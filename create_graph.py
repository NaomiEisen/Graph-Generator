import argparse

from test_handlers.nv_bandwidth import start_nvbandwith
from utils.handle_data import get_files_list
from utils.parse_file import TestsType, determine_test_type


def main():
    # mapping for different tests graph generators
    test_function_map = {
    TestsType.NV_BANDWIDTH_TYPE :start_nvbandwith
    }  
        
    parser = argparse.ArgumentParser(description="Plot data from a file.")
    parser.add_argument("files", nargs='+', help="File names or directories for the input data")
    args = parser.parse_args()

    # collect the files
    files = get_files_list(args.files)

    for file in files:
        test_type= determine_test_type(file)
        print(test_type) # TODO: delete later!

        func = test_function_map.get(test_type)
        if func:
            func(file)


if __name__ == "__main__":
    main()
    
