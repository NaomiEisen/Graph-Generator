import argparse

from data_structures.device_bw_struct import DeviceBw
from data_structures.nv_bandwidth_struct import NvBandwidth
from graph_generators.global_plot_config import update_plot_config
from test_handlers.bw_gpu import start_bw_gpu, plot_all_files_together
from test_handlers.nv_bandwidth import start_bandwidth, plot_opt_vs_org
from utils.handle_data import get_files_list
from utils.parse_file import TestsType, determine_test_type


def main():
    # mapping for different tests graph generators
    test_function_map = {
    TestsType.NV_BANDWIDTH_TYPE :start_bandwidth,
    TestsType.GPU_BANDWIDTH_TYPE: start_bw_gpu
    }  
        
    parser = argparse.ArgumentParser(description="Plot data from files.")
    parser.add_argument("files", nargs='+', help="File names or directories for the input data")
    args = parser.parse_args()

    # collect the files
    files = get_files_list(args.files)

    struct_dict = {}

    # prepare plot config
    update_plot_config()

    for file in files:
        test_type= determine_test_type(file)
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
        plot_all_files_together(gpus_bw)

    # Plot opt vs org bandwidth tests
    nvbandwidth = struct_dict.get(NvBandwidth)
    if nvbandwidth:
        # plot opt vs org
        plot_opt_vs_org(nvbandwidth)




if __name__ == "__main__":
    main()
    
