import argparse

from globals import GeneratorScripts
# from graph_generators.old.bw_all_gpus import bandwidth_all_gpu_test
# from graph_generators.old.bw_avg import bandwidth_avg_gpu
# from graph_generators.generic import plot_data_from_files
# from graph_generators.old.nccl import nccl_test_graph
from test_handles.nv_bandwidth import start_nvbandwith
from helpers.handle_data import get_files_list
from helpers.parse_file import TestsType, determine_test_type


def main():
    # mapping for different tests graph generators
    test_function_map = {
    # GeneratorScripts.NCCL: nccl_test_graph,
    # GeneratorScripts.BANDWIDTH_GPU_AVG: bandwidth_avg_gpu,
    # GeneratorScripts.BANDWIDTH_GPU_ALL: bandwidth_all_gpu_test,
    # GeneratorScripts.GENERIC: plot_data_from_files,

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
    
