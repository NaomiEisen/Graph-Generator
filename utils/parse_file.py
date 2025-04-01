import os

# Helper class to determine the test based on the file's content
class TestsType:
    NV_BANDWIDTH_TYPE = "nvbandwidth"
    GPU_BANDWIDTH_TYPE = "bandwidthtest"
    ALL_REDUCE_TYPE = "nccl"

def determine_test_type(file_path):
    """
    Determines the test type based on the first line of the file.
    """
    try:
        with open(file_path, 'r') as file:
            first_line = file.readline().strip().lower()  # Read first line and normalize case

            if TestsType.ALL_REDUCE_TYPE in first_line:
                return TestsType.ALL_REDUCE_TYPE
            elif TestsType.NV_BANDWIDTH_TYPE in first_line:
                return TestsType.NV_BANDWIDTH_TYPE 
            elif TestsType.GPU_BANDWIDTH_TYPE in first_line:
                return TestsType.GPU_BANDWIDTH_TYPE
            else:
                return "UNKNOWN"
    except Exception as e:
        print(f"Error reading file {file_path}: {e}")
        return "ERROR"


def get_files_list(args):
    """
    Recursively collects all files from directories, including nested ones.
    If an argument is already a file, it is added as-is.
    """
    files = []

    for file in args:
        if isinstance(file, str) and os.path.isdir(file):
            # Walk through all subdirectories and collect files
            for root, _, filenames in os.walk(file):
                for f in filenames:
                    files.append(os.path.join(root, f))
        else:
            # If it's already a file, add it directly
            files.append(file)

    return files