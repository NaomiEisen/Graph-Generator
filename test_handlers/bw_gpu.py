from collections import defaultdict
import inspect
import pandas as pd

from data_structures.device_bw_struct import DeviceBw
from data_structures.test import Test
from graph_generators.plot import plot_graph
from graphs_config import GpuBandwidthGraphConfig
from tests_config.tests_config_gpu_bw import GpuBwConfig
from utils.general import get_filename_without_extension
from utils.handle_data import load_data_two_column


def create_test_instance_and_plot(bw_struct, configs, final_name, test_name):
    # Load and combine test data
    tests_to_combine = [parse_data_from_test_config(config, bw_struct) for config in configs]
    combined_data = combine_data_frame(tests_to_combine)

    if combined_data.empty:
        return  # Return if there is no data to process

    # Debugging print (remove later if not needed)
    print("Combined!")
    print(combined_data)

    # Create bar graph
    plot_graph(combined_data, GpuBandwidthGraphConfig, get_filename_without_extension(bw_struct.org_file) + final_name, test_name)

    # Append results to nv_bandwidth_struct
    bw_struct.add_test(Test(name=final_name, activate="true", data_pandas=combined_data))


def parse_data_from_test_config(test_config, nv_bandwidth_struct):
    # Check if the test is activated
    if test_config["activate"]:
        # Create the test from the configuration
        test = Test.test_from_config(test_config)
        
        # Parse the test data from the given file
        test.parse_test_data(nv_bandwidth_struct.org_file, test_config["right_offset"], load_data_two_column)

        # Change the name of the second column to 'bandwidth'
        test.data_pandas.columns = [test.data_pandas.columns[0], test_config["name"]] + list(test.data_pandas.columns[2:])

        # Print the result
        print(test.data_pandas)

        return test
    
    else:
        return None

    
def combine_data_frame(tests):
    valid_dfs = [test.data_pandas for test in tests
                 if test is not None and test.data_pandas is not None and not test.data_pandas.empty]

    combined_df = valid_dfs[0].copy()

    for df in valid_dfs[1:]:
        if df.shape[1] > 1:  # Ensure the DataFrame has at least 2 columns
            second_column = df.iloc[:, 1]  # Extract the second column
            column_name = df.columns[1]  # Use the original column header

            # Append the column to the combined DataFrame
            combined_df[column_name] = second_column.reset_index(drop=True)

    return combined_df


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
    print(grouped_test_configs)

    for config_group in grouped_test_configs:
        create_test_instance_and_plot(bw_struct, config_group, GpuBwConfig.FILE_NAME, GpuBwConfig.TEST_NAME)
    
    return bw_struct
