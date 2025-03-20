import pandas as pd

from graphs_config import NvBandwidthGraphConfig
from data_structures.nv_bandwidth_struct import NvBandwidth
from data_structures.test import Test
from test_handlers.test_handlers_utils import groups_all_configs
from tests_config.tests_config_nvbw import NvBandwidthConfig
from graph_generators.bar_graph import plot_bar_graph
from utils.general import get_filename_without_extension
from utils.handle_data import load_data_matrix_format


def create_test_instance_and_plot(nv_bandwidth_struct, configs, final_name, test_name):
    """
    Loads test data for multiple configurations, combines them into a single DataFrame,
    modifies column names, and generates a bar graph.
    """
    # Load and combine test data
    tests_to_combine = [parse_data_from_test_config(config, nv_bandwidth_struct) for config in configs]
    combined_data = combine_data_frame(tests_to_combine)

    if combined_data.empty:
        return  # Return if there is no data to process

    # Append 'gpu' to each column name where needed
    add_prefix(combined_data, 'GPU')

    # Debugging print (remove later if not needed)
    print(combined_data)

    # Create bar graph
    plot_bar_graph(combined_data, NvBandwidthGraphConfig, get_filename_without_extension(nv_bandwidth_struct.org_file) + final_name, test_name)

    # Append results to nv_bandwidth_struct
    nv_bandwidth_struct.add_test(Test(name=final_name, activate="true", data_pandas=combined_data))


def add_prefix(combined_data, prefix):
    for col in combined_data.columns:
        if pd.to_numeric(combined_data[col], errors='coerce').notna().all():
            combined_data.rename(columns={col: prefix + col}, inplace=True)


def parse_data_from_test_config(test_config, nv_bandwidth_struct):
    # Check if the test is activated
    if test_config["activate"]:
        # Create the test from the configuration
        test = Test.test_from_config(test_config)
        
        # Parse the test data from the given file
        test.parse_test_data(nv_bandwidth_struct.org_file, test_config["right_offset"], load_data_matrix_format)

        # Process data by its format
        if test.data_pandas.shape[0] > 1:
            # Calculate the overall average for all values in the DataFrame, ignoring NaN values
            overall_avg = test.data_pandas.stack().mean()

            # Create a new DataFrame with 'overall_avg' as index and the average value as the column
            avg_df = pd.DataFrame({'average bandwidth (GB/s)': [overall_avg]}, index=[test.name])
            test.data_pandas = avg_df

        else:
             # Set the custom index for the data
            test.data_pandas.index = [test_config["name"]]  # Set custom index from the config
        
        # Print the result
        print(test.data_pandas)

        return test
    
    else:
        return None
        
    
def combine_data_frame(tests):
    # Filter out None values or empty data_pandas attributes
    valid_dfs = [test.data_pandas for test in tests if test is not None and test.data_pandas is not None and not test.data_pandas.empty]
    
    # Combine the DataFrames if there are any valid ones, else return an empty DataFrame
    return pd.concat(valid_dfs, axis=0) if valid_dfs else pd.DataFrame()


def start_bandwidth(file):
    nv_bandwidth_struct = NvBandwidth(org_file=file)

    grouped_test_configs = groups_all_configs(NvBandwidthGraphConfig)
    for config_group in grouped_test_configs:
        group_id = config_group[0]['group_id']  # Get group_id from the first config in the group
        group_info = NvBandwidthConfig.GROUPS_INFO[group_id]  # Lookup group info
        create_test_instance_and_plot(nv_bandwidth_struct, config_group, group_info["file_name"], group_info["test_name"])
    
    return nv_bandwidth_struct