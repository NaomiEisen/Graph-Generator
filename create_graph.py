import argparse

from utils.set_users_args import set_output_folder, set_colors, set_v2_identifier
from data_structures.all_reduce_struct import AllReduce
from data_structures.device_bw_struct import DeviceBw
from data_structures.nv_bandwidth_struct import NvBandwidth
from graph_generators.global_plot_config import set_costume_global_plot_settings
from test_handlers.bw_gpu import start_bw_gpu, plot_gpu_bandwidth_average
from test_handlers.nv_bandwidth import start_bandwidth, plot_nvbandwidth_comparison
from test_handlers.all_reduce import start_reduce_all, plot_all_reduce_comparison
from utils.parse_file import get_files_list
from utils.parse_file import TestsType, determine_test_type

def plot_all_files(file_list):
    # mapping for different tests graph generators
    test_function_map = {
        TestsType.NV_BANDWIDTH_TYPE: start_bandwidth,
        TestsType.GPU_BANDWIDTH_TYPE: start_bw_gpu,
        TestsType.ALL_REDUCE_TYPE: start_reduce_all
    }

    # Organize file test if the corresponding struct when finished
    struct_dict = {}

    for file in file_list:
        test_type = determine_test_type(file)
        func = test_function_map.get(test_type)
        if func:
            test_struct = func(file)

            # Get the class of the struct
            struct_class = type(test_struct)

            # Add the struct to the dictionary under its class
            if struct_class not in struct_dict:
                struct_dict[struct_class] = []
            struct_dict[struct_class].append(test_struct)

    # Plot avg of all bandwidth tests
    gpus_bw = struct_dict.get(DeviceBw)
    if gpus_bw:
        plot_gpu_bandwidth_average(gpus_bw)

    return struct_dict

def plot_comparisons(struct_dict):
    comparison_function_map = {
        NvBandwidth: plot_nvbandwidth_comparison,
        AllReduce: plot_all_reduce_comparison
    }

    # Plot comparison graphs for each class in the dict
    for struct_class, struct_list in struct_dict.items():
        if struct_class in comparison_function_map:
            comparison_function_map[struct_class](struct_list)

def handle_args():
    parser = argparse.ArgumentParser(description="Plot data from files.")
    parser.add_argument("files", nargs='+',
                        help="File names or directories for the input data")
    parser.add_argument("-o", "--output-dir", default=None,
                        help="Directory to save output plots (optional)")
    parser.add_argument("--colors", type=str, nargs=2, choices=['orange', 'turquoise', 'purple', 'red', 'green', 'pink'],
                        help="Specify colors to be used for plots. Allowed values: orange, turquoise, purple, red, green, pink.")
    parser.add_argument("--v2-identifier", "--v2", type=str, nargs=1,
                        help="Specify the identifier for the v2 tests.")

    args = parser.parse_args()

    # Set the versions colors if provided
    if args.colors:
        set_colors(args.colors)

    # Set the output directory if provided
    if args.output_dir:
        set_output_folder(args.output_dir)

    if args.v2_identifier:
        print(f"Setting v2 identifier to {args.v2_identifier}")
        set_v2_identifier(args.v2_identifier)


    return args


def main():
    args = handle_args()
    files = get_files_list(args.files)  # collect the files
    set_costume_global_plot_settings()  # Set the default plot settings

    tests_structs_dict = plot_all_files(files)
    plot_comparisons(tests_structs_dict)

if __name__ == "__main__":
    main()
    
