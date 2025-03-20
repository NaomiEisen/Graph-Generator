
class TestsType:
    NCCL_TYPE = "nccl"
    NV_BANDWIDTH_TYPE = "nvbandwidth"
    GPU_BANDWIDTH_TYPE = "bandwidthtest"


def determine_test_type(file_path):
    """
    Determines the test type based on the first line of the file.

    Args:
        file_path (str): Path to the file.

    Returns:
        str: "NCCL" if 'nccl' appears in the first line,
             "NV_BANDWIDTH" if 'nvbandwidth' appears,
             "UNKNOWN" otherwise.
    """
    try:
        with open(file_path, 'r') as file:
            first_line = file.readline().strip().lower()  # Read first line and normalize case

            if TestsType.NCCL_TYPE in first_line:
                return TestsType.NCCL_TYPE
            elif TestsType.NV_BANDWIDTH_TYPE in first_line:
                return TestsType.NV_BANDWIDTH_TYPE 
            elif TestsType.GPU_BANDWIDTH_TYPE in first_line:
                return TestsType.GPU_BANDWIDTH_TYPE
            else:
                return "UNKNOWN"
    except Exception as e:
        print(f"Error reading file {file_path}: {e}")
        return "ERROR"
    

def get_test_range(file_path, start_text, end_text, offset=0):
    """
    Finds the range of lines between start_text and end_text in a file.

    Args:
        file_path (str): Path to the file.
        start_text (str): The text marking the start of the range.
        end_text (str): The text marking the end of the range.
        offset (int): Number of lines to shift the start index forward.

    Returns:
        tuple: 
            - (start_index, end_index) if both texts are found.  
            - (None, None) if not found.  
    """
    start_index = None
    end_index = None

    with open(file_path, 'r') as f:
        lines = f.readlines()

    for i, line in enumerate(lines):
        if start_text in line and start_index is None:
            start_index = i + offset
        elif end_text in line:
            end_index = i
            break  # Stop searching after finding the end text

    if start_index is not None and end_index is not None and start_index < end_index:
        return start_index, end_index
    return None, None  # Return None if range is invalid





