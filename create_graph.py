import argparse

from configs.output_dir import set_output_folder
from data_structures.device_bw_struct import DeviceBw
from data_structures.nv_bandwidth_struct import NvBandwidth
from graph_generators.global_plot_config import set_costume_global_plot_settings
from test_handlers.bw_gpu import start_bw_gpu, plot_gpu_bandwidth_averege
from test_handlers.nv_bandwidth import start_bandwidth, plot_nvbandwidth_comparison
from test_handlers.all_reduce import start_reduce_all
from utils.parse_file import get_files_list
from utils.parse_file import TestsType, determine_test_type

def plot_all_files(file_list):
    # mapping for different tests graph generators
    test_function_map = {
        TestsType.NV_BANDWIDTH_TYPE: start_bandwidth,
        TestsType.GPU_BANDWIDTH_TYPE: start_bw_gpu,
        TestsType.ALL_REDUCE_TYPE: start_reduce_all
    }

    struct_dict = {}  # Organize file test if the corresponding struct when finished

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
        plot_gpu_bandwidth_averege(gpus_bw)

    return struct_dict

def plot_comparisons(struct_dict):
    # Plot comparison for nvbandwidth test
    nvbandwidth = struct_dict.get(NvBandwidth)
    if nvbandwidth:
        # plot opt vs org
        plot_nvbandwidth_comparison(nvbandwidth)


def main():
    # Parse arguments
    parser = argparse.ArgumentParser(description="Plot data from files.")
    parser.add_argument("files", nargs='+', help="File names or directories for the input data")
    parser.add_argument("-o", "--output-dir", default=None, help="Directory to save output plots (optional)")

    args = parser.parse_args()
    files = get_files_list(args.files) # collect the files
    set_costume_global_plot_settings() # Set the default plot settings

    # Get the output directory
    output_dir = args.output_dir
    if output_dir:
        set_output_folder(output_dir)

    struct_dict = plot_all_files(files)
    plot_comparisons(struct_dict)

if __name__ == "__main__":
    main()
    
