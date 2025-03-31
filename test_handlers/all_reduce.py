from configs.all_reduce_configs.graph_config_all_reduce import AllReduceGraphConfig
from configs.all_reduce_configs.test_config_all_reduce import AllReduceConfig
from data_structures.all_reduce_struct import AllReduce
from data_structures.test import Test
from graph_generators.plot import plot_two_subplots
from test_handlers.handle_comparison import get_two_versions
from utils.general import replace_underscores_with_spaces, get_filename_without_extension
from utils.handle_data import load_data_matrix_format


def create_test_instance_and_plot(all_reduce_struct):
    # Load data by the only config of this test
    test = Test.test_from_config(AllReduceConfig.ALL_REDUCE)

    # Parse the test data from the given file
    test.parse_test_data(all_reduce_struct.org_file, AllReduceConfig.ALL_REDUCE["right_offset"], load_data_matrix_format)

    plot_two_subplots(
        test.data_pandas,
        graph_config=AllReduceGraphConfig,
        file_name=get_filename_without_extension(all_reduce_struct.org_file),
        test_name=replace_underscores_with_spaces(AllReduceConfig.FILE_NAME))

    # Extract columns for optional comparison
    df_to_compare = extract_averege_columns(test.data_pandas)

    # Append results to nv_bandwidth_struct
    all_reduce_struct.add_test(Test(AllReduceConfig.ALL_REDUCE["name"], activate="true", data_pandas=df_to_compare))


def extract_averege_columns(data_pandas):

    # return data_pandas[['size', 'tavg', 'avgbw']]
    return data_pandas[AllReduceConfig.COLUMNS_TO_COMPARE]

def plot_all_reduce_comparison(all_reduce_struct_list):
    v1_struct, v2_struct = get_two_versions(all_reduce_struct_list)
    v1_tests = v1_struct.get_test()
    v2_tests = v2_struct.get_test()



def start_reduce_all(file):
    # TODO: check only for file name- not the whole path
    if '2' in file:
        reduce_all_struct = AllReduce(org_file=file, file_version= AllReduce.TYPE_V2)
    else:
        reduce_all_struct = AllReduce(org_file=file, file_version=AllReduce.TYPE_V1)

    print("found reduce all")
    create_test_instance_and_plot(reduce_all_struct)

    return reduce_all_struct