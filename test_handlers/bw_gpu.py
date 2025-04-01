from data_structures.device_bw_struct import DeviceBw
from data_structures.test import Test
from graph_generators.plot import plot_single_lines_graph
from configs.gpu_bandwidth_configs.graph_config_gpu_bw import GpuBandwidthGraphConfig
from test_handlers.test_handlers_utils import groups_all_configs
from configs.gpu_bandwidth_configs.tests_config_gpu_bw import GpuBwConfig
from utils.general import get_filename_without_extension, replace_underscores_with_spaces
from utils.handle_data import load_data_two_column

def plot_gpu_bandwidth_average(tests):
    # get avg for each col of all the different tests and create new data frame
    avg_df = calculate_avg_of_all_tests(tests)

    # Create plot graph
    plot_single_lines_graph(avg_df, GpuBandwidthGraphConfig, "bandwidth_gpu_bw_average",
               "Bandwidth Test Average")

def calculate_avg_of_all_tests(gpu_bw_struct_list):
    dataframes = [gpu_bw_struct.Test.data_pandas for gpu_bw_struct in gpu_bw_struct_list]

    # Sum all the DataFrames
    sum_df = sum(dataframes)

    # Calculate the average by dividing by the number of DataFrames
    avg_df = sum_df / len(dataframes)

    return avg_df

def create_test_instance_and_plot(bw_struct, configs, final_name):
    # Load and combine test data
    tests_to_combine = [parse_data_from_test_config(config, bw_struct) for config in configs]
    combined_data = combine_data_frame(tests_to_combine)

    if combined_data.empty:
        return  # Return if there is no data to process

    # Append results to nv_bandwidth_struct
    bw_struct.Test = (Test(name=final_name, activate="true", data_pandas=combined_data))

    file_name = get_filename_without_extension(bw_struct.org_file)
    graph_title = replace_underscores_with_spaces(file_name)

    # Create plot graph
    plot_single_lines_graph(combined_data, GpuBandwidthGraphConfig, file_name, graph_title)


def parse_data_from_test_config(test_config, nv_bandwidth_struct):
    # Check if the test is activated
    if test_config["activate"]:
        # Create the test from the configuration
        test = Test.test_from_config(test_config)
        
        # Parse the test data from the given file
        test.parse_test_data(nv_bandwidth_struct.org_file, test_config["right_offset"], load_data_two_column)

        # Change the name of the second column to 'bandwidth'
        test.data_pandas.columns = [test.data_pandas.columns[0], test_config["name"]] + list(test.data_pandas.columns[2:])

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

    # groups all configs by group id
    grouped_test_configs = groups_all_configs(GpuBwConfig)

    for config_group in grouped_test_configs:
        create_test_instance_and_plot(bw_struct, config_group, GpuBwConfig.FILE_NAME)
    
    return bw_struct
