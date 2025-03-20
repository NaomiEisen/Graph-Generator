import pandas as pd

from data_structures.device_bw_struct import DeviceBw
from data_structures.test import Test
from graph_generators.plot import plot_graph
from graphs_config import GpuBandwidthGraphConfig
from test_handlers.test_handlers_utils import groups_all_configs
from tests_config.tests_config_gpu_bw import GpuBwConfig
from utils.general import get_filename_without_extension
from utils.handle_data import load_data_two_column

def plot_all_files_together(bw_struct):
    # get avg for each col of all the different tests and create new data frame
    tests = bw_struct.get_tests()

    avg_df = calculate_avg_of_all_tests(tests)

    # Create plot graph
    plot_graph(avg_df, GpuBandwidthGraphConfig, get_filename_without_extension(bw_struct.org_file) + "avg",
               "avg")

    print(avg_df)

import pandas as pd

def calculate_avg_of_all_tests(tests):
    # Initialize empty lists to store the values from all tests
    all_columns_data = {col: [] for col in tests[0].data_pandas.columns[1:]}  # Skip the first column

    # Loop through each test in the tests list
    for test in tests:
        # Loop through each column in the test data (skip the first column)
        for col in test.data_pandas.columns[1:]:  # Skip the first column
            all_columns_data[col].append(test.data_pandas[col])

    # Create a new DataFrame to store the averages for each column
    avg_columns = {col: [sum(x) / len(x) for x in zip(*all_columns_data[col])] for col in all_columns_data}

    # Create a new DataFrame with the averages, keeping the same column names as the original data
    avg_df = pd.DataFrame(avg_columns)

    # Get the first column from tests[0] and its header
    first_col = tests[0].data_pandas[tests[0].data_pandas.columns[0]]

    # Concatenate the first column (with its header) to the beginning of avg_df
    avg_df = pd.concat([first_col, avg_df], axis=1)

    return avg_df


def create_test_instance_and_plot(bw_struct, configs, final_name, test_name):
    # Load and combine test data
    tests_to_combine = [parse_data_from_test_config(config, bw_struct) for config in configs]
    combined_data = combine_data_frame(tests_to_combine)

    if combined_data.empty:
        return  # Return if there is no data to process

    # Create plot graph
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


def start_bw_gpu(file):
    bw_struct = DeviceBw(org_file=file)

    grouped_test_configs = groups_all_configs(GpuBwConfig)
    print(grouped_test_configs)

    for config_group in grouped_test_configs:
        create_test_instance_and_plot(bw_struct, config_group, GpuBwConfig.FILE_NAME, GpuBwConfig.TEST_NAME)
    
    return bw_struct
