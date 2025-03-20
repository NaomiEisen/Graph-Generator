import argparse

from data_structures.device_bw_struct import DeviceBw
from test_handlers.bw_gpu import start_bw_gpu, start_bw_gpu, plot_all_files_together
from test_handlers.nv_bandwidth import start_bandwidth
from utils.handle_data import get_files_list
from utils.parse_file import TestsType, determine_test_type


def main():
    # mapping for different tests graph generators
    test_function_map = {
    TestsType.NV_BANDWIDTH_TYPE :start_bandwidth,
    TestsType.GPU_BANDWIDTH_TYPE: start_bw_gpu
    }  
        
    parser = argparse.ArgumentParser(description="Plot data from a file.")
    parser.add_argument("files", nargs='+', help="File names or directories for the input data")
    args = parser.parse_args()

    # collect the files
    files = get_files_list(args.files)

    struct_dict = {}

    for file in files:
        test_type= determine_test_type(file)
        func = test_function_map.get(test_type)
        if func:
            test_struct = func(file)

            # Get the class of the struct
            struct_class = type(test_struct)

            if struct_class == DeviceBw:
                plot_all_files_together(test_struct)
                # tests = test_struct.get_tests()
                # print('------------------------------')
                # print(len(tests))
                # for test in tests:
                #     print(test)
                #     print("\n")


            # Add the struct to the dictionary under its class
            if struct_class not in struct_dict:
                struct_dict[struct_class] = []  # Create a new list for this class
            struct_dict[struct_class].append(test_struct)

    #print(struct_dict)


if __name__ == "__main__":
    main()
    
