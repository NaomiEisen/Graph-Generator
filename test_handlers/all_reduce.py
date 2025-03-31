from configs.all_reduce_configs.graph_config_all_reduce import AllReduceGraphConfig
from configs.all_reduce_configs.test_config_all_reduce import AllReduceConfig
from data_structures.all_reduce_struct import AllReduce
from data_structures.test import Test
from graph_generators.plot import plot_two_subplots
from utils.general import replace_underscores_with_spaces
from utils.handle_data import load_data_matrix_format


def create_test_instance_and_plot(all_reduce_struct):
    # Load data by the only config of this test
    test = Test.test_from_config(AllReduceConfig.ALL_REDUCE)

    # Parse the test data from the given file
    test.parse_test_data(all_reduce_struct.org_file, AllReduceConfig.ALL_REDUCE["right_offset"], load_data_matrix_format)

    # Append results to nv_bandwidth_struct
    all_reduce_struct.add_test(Test(name=AllReduceConfig.FILE_NAME, activate="true", data_pandas=test.data_pandas))

    plot_two_subplots(
        all_reduce_struct.Test.data_pandas,
        graph_config=AllReduceGraphConfig,
        file_name=AllReduceConfig.FILE_NAME+"second",
        test_name=replace_underscores_with_spaces(AllReduceConfig.FILE_NAME))


def start_reduce_all(file):
    # TODO: check only for file name- not the whole path
    if '2' in file:
        reduce_all_struct = AllReduce(org_file=file, type_file= AllReduce.TYPE_V2)
    else:
        reduce_all_struct = AllReduce(org_file=file, type_file=AllReduce.TYPE_V1)

    print("found reduce all")
    create_test_instance_and_plot(reduce_all_struct)

    return reduce_all_struct