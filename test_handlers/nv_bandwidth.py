import pandas as pd

from data_structures.test_verion import TestVersion
from graph_generators.comparison_graphs import comparison_bar_graph
from configs.nvbandwidth_configs.graph_config_nvbandwidth import NvBandwidthGraphConfig, NvBandwidthCompareGraphConfig
from data_structures.nv_bandwidth_struct import NvBandwidth
from data_structures.test import Test
from test_handlers.handle_comparison import get_two_versions
from test_handlers.test_handlers_utils import groups_all_configs
from configs.nvbandwidth_configs.tests_config_nvbw import NvBandwidthConfig
from graph_generators.bar_graph import plot_bar_graph
from utils.general import replace_underscores_with_spaces
from utils.handle_data import load_data_matrix_format
from utils.set_users_args import UserArgs


def plot_nvbandwidth_comparison(bandwidth_struct_list):
    bandwidth_struct_v1, bandwidth_struct_v2 = get_two_versions(bandwidth_struct_list)

    v2_tests = bandwidth_struct_v2.get_tests()
    v1_tests = bandwidth_struct_v1.get_tests()

    for v2_test in v2_tests:  # Iterate through each test in opt_tests
        # Find a test in v1_tests with the same name
        matching_v1_test = next((v1_test for v1_test in v1_tests if v1_test.name == v2_test.name), None)

        if matching_v1_test is not None:
            comparison_bar_graph(
                data_v1= matching_v1_test.data_pandas,
                data_v2= v2_test.data_pandas,
                graph_config= NvBandwidthCompareGraphConfig,
                test_name= replace_underscores_with_spaces(f"{v2_test.name} {NvBandwidthCompareGraphConfig.TITLE}"),
                file_name= f"{NvBandwidthCompareGraphConfig.OUTPUT_FILE_PREFIX}{v2_test.name}")

        else:
            print(f"Test {v2_test.name} not found in both of the versions.")

def create_test_instance_and_plot(nv_bandwidth_struct, configs, graph_file_name, test_name):
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

    # Create bar graph
    file_name = graph_file_name + UserArgs.V2_IDENTIFIER if nv_bandwidth_struct.version == TestVersion.V2 else graph_file_name
    plot_bar_graph(combined_data, NvBandwidthGraphConfig, file_name, test_name, nv_bandwidth_struct.version)

    # Append results to nv_bandwidth_struct
    nv_bandwidth_struct.add_test(Test(name=graph_file_name, activate="true", data_pandas=combined_data))


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
        if test.data_pandas is None:
            return None# Didn't find the desired test - just ignore it

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

    grouped_test_configs = groups_all_configs(NvBandwidthConfig)
    for config_group in grouped_test_configs:
        config = config_group[0]  # First item in the group
        group_id = config.get('group_id')  # Returns None if key doesn't exist

        if group_id is not None and group_id in NvBandwidthConfig.GROUPS_INFO:
            group_info = NvBandwidthConfig.GROUPS_INFO[group_id]
            create_test_instance_and_plot(nv_bandwidth_struct, config_group, group_info["file_name"],
                                          group_info["test_name"])
        else:
            create_test_instance_and_plot(nv_bandwidth_struct, config_group, config["name"], config["name"])

    return nv_bandwidth_struct