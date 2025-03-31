import pandas as pd

from configs.comparison_config import ComparisonGraphConfig
from data_structures.test_verion import TestVersion
from graph_generators.comparison_graph import comparison_bar_graph_nvbandwidth
from configs.nvbandwidth_configs.graph_config_nvbandwidth import NvBandwidthGraphConfig
from data_structures.nv_bandwidth_struct import NvBandwidth
from data_structures.test import Test
from test_handlers.handle_comparison import get_two_versions
from test_handlers.test_handlers_utils import groups_all_configs
from configs.nvbandwidth_configs.tests_config_nvbw import NvBandwidthConfig
from graph_generators.bar_graph import plot_bar_graph
from utils.general import replace_underscores_with_spaces
from utils.handle_data import load_data_matrix_format


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
    file_name = 'v2_' + graph_file_name if nv_bandwidth_struct.version == TestVersion.V2 else graph_file_name
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
    # TODO: check only for file name- not the whole path
    if '2' in file:
        nv_bandwidth_struct = NvBandwidth(org_file=file, file_version= TestVersion.V2)
    else:
        nv_bandwidth_struct = NvBandwidth(org_file=file, file_version= TestVersion.V1)

    grouped_test_configs = groups_all_configs(NvBandwidthConfig)
    for config_group in grouped_test_configs:
        group_id = config_group[0]['group_id']  # Get group_id from the first config in the group
        group_info = NvBandwidthConfig.GROUPS_INFO[group_id]  # Lookup group info
        create_test_instance_and_plot(nv_bandwidth_struct, config_group, group_info["file_name"], group_info["test_name"])
    
    return nv_bandwidth_struct


def plot_nvbandwidth_comparison(bandwidth_struct_list):
    bandwidth_struct_v1, bandwidth_struct_v2 = get_two_versions(bandwidth_struct_list)

    v2_tests = bandwidth_struct_v2.get_tests()
    v1_tests = bandwidth_struct_v1.get_tests()

    for opt_test in v2_tests:  # Iterate through each test in opt_tests
        # Find a test in org_tests with the same name
        matching_org_test = next((org_test for org_test in v1_tests if org_test.name == opt_test.name), None)

        if matching_org_test is not None:
            print(f"Comparing opt {opt_test.name} with org {matching_org_test.name}")
            comparison_bar_graph_nvbandwidth(
                data_v1= matching_org_test.data_pandas,
                data_v2= opt_test.data_pandas,
                graph_config= ComparisonGraphConfig,
                test_name= replace_underscores_with_spaces(f"{opt_test.name} {ComparisonGraphConfig.TITLE}"),
                file_name= f"{ComparisonGraphConfig.OUTPUT_FILE_PREFIX}{opt_test.name}")

        else:
            print(f"Test {opt_test.name} not found in org_tests")