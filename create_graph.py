import argparse

from globals import GeneratorScripts
from graph_generators.bw_all_gpus import bandwidth_all_gpu_test
from graph_generators.bw_avg import bandwidth_avg_gpu
from graph_generators.generic import plot_data_from_files
from graph_generators.nccl import nccl_test_graph


def main():
    parser = argparse.ArgumentParser(description="Plot data from a file.")
    parser.add_argument("test_primitive", help="Test primitive type (e.g. nccl_test, bandwidth_test, bandwidth_avg_test)")
    parser.add_argument("file_names", nargs='+', help="File names for the input data")

    args = parser.parse_args()

    test_function_map = {
    GeneratorScripts.NCCL: nccl_test_graph,
    GeneratorScripts.BANDWIDTH_GPU_AVG: bandwidth_avg_gpu,
    GeneratorScripts.BANDWIDTH_GPU_ALL: bandwidth_all_gpu_test,
    GeneratorScripts.GENERIC: plot_data_from_files
    }   

    func = test_function_map.get(args.test_primitive)
    if func:
        func(args.file_names)


if __name__ == "__main__":
    main()
    
