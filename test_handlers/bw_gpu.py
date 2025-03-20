from collections import defaultdict
import inspect
import pandas as pd

from data_structures.device_bw_struct import DeviceBw
from data_structures.test import Test
from tests_config.tests_config_gpu_bw import GpuBwConfig
from graph_generators.bar_graph import plot_bar_graph
from utils.general import get_filename_without_extension


def create_test_instance_and_plot(nv_bandwith_struct, configs, final_name, test_name):
    # Load and combine test data
    tests_to_combine = [parse_data_from_test_config(config, nv_bandwith_struct) for config in configs]
    combined_data = combine_data_frame(tests_to_combine)

    if combined_data.empty:
        return  # Return if there is no data to process

    # Append 'gpu' to each column name where needed
    add_prefix(combined_data, 'GPU')

    # Debugging print (remove later if not needed)
    print(combined_data)

    # Create bar graph
    #plot_bar_graph(combined_data, NvBandwidthGraphConfig, get_filename_without_extension(nv_bandwith_struct.org_file) + final_name, test_name)

    # Append results to nv_bandwith_struct
    nv_bandwith_struct.add_test(Test(name=final_name, activate="true", data_pandas=combined_data))

def add_prefix(combined_data, prefix):
    for col in combined_data.columns:
        if pd.to_numeric(combined_data[col], errors='coerce').notna().all():
            combined_data.rename(columns={col: prefix + col}, inplace=True)


def parse_data_from_test_config(test_config, nv_bandwith_struct):
    # Check if the test is activated
    if test_config["activate"]:
        # Create the test from the configuration
        test = Test.test_from_config(test_config)
        
        # Parse the test data from the given file
        test.parse_test_data(nv_bandwith_struct.org_file)

        # Process data by it's format
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

def group_configs():
    grouped_configs = defaultdict(list)

    # Get all class attributes
    for name, value in inspect.getmembers(GpuBwConfig):
        # Ensure it's a dictionary and has 'group_id'
        if isinstance(value, dict) and 'group_id' in value:
            grouped_configs[value['group_id']].append(value)

    # Convert to list of lists
    return list(grouped_configs.values())


def start_bw_gpu(file):
    bw_struct = DeviceBw(org_file=file)

    grouped_test_configs = group_configs()
    for config_group in grouped_test_configs:
        create_test_instance_and_plot(bw_struct, config_group, "file", "test")
    
    return bw_struct
