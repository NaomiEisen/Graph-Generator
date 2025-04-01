from configs.all_reduce_configs.graph_config_all_reduce import AllReduceGraphConfig, AllReduceCompareGraphConfig
from configs.all_reduce_configs.test_config_all_reduce import AllReduceConfig
from data_structures.all_reduce_struct import AllReduce
from data_structures.test import Test
from data_structures.test_verion import TestVersion
from graph_generators.comparison_graphs import comparison_line_graph
from graph_generators.plot import plot_subplots_line_graph
from test_handlers.handle_comparison import get_two_versions
from utils.general import replace_underscores_with_spaces, get_filename_without_extension
from utils.handle_data import load_data_matrix_format
from utils.set_users_args import UserArgs


def create_test_instance_and_plot(all_reduce_struct):
    # Load data by the only config of this test
    test = Test.test_from_config(AllReduceConfig.ALL_REDUCE)

    # Parse the test data from the given file
    test.parse_test_data(all_reduce_struct.org_file, AllReduceConfig.ALL_REDUCE["right_offset"], load_data_matrix_format)

    graphs_file_name = AllReduceConfig.FILE_NAME
    if all_reduce_struct.version == TestVersion.V2:
        graphs_file_name += "_"+UserArgs.V2_IDENTIFIER

    plot_subplots_line_graph(
        test.data_pandas,
        graph_config=AllReduceGraphConfig,
        file_name= graphs_file_name)

    # Extract columns for optional comparison
    df_to_compare = extract_averege_columns(test.data_pandas)

    # Append results to nv_bandwidth_struct
    all_reduce_struct.Test = (Test(AllReduceConfig.ALL_REDUCE["name"], activate="true", data_pandas=df_to_compare))


def extract_averege_columns(data_pandas):
    return data_pandas[AllReduceConfig.COLUMNS_TO_COMPARE]

def plot_all_reduce_comparison(all_reduce_struct_list):
    v1_struct, v2_struct = get_two_versions(all_reduce_struct_list)
    print(v1_struct.Test.data_pandas)
    print(v2_struct.Test.data_pandas)
    comparison_line_graph(
        v1_struct.Test.data_pandas,
        v2_struct.Test.data_pandas,
        AllReduceCompareGraphConfig,
        AllReduceCompareGraphConfig.FILE_NAME
    )


def start_reduce_all(file):
    reduce_all_struct = AllReduce(org_file=file)
    print("found reduce all")
    create_test_instance_and_plot(reduce_all_struct)

    return reduce_all_struct