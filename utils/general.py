import os
from configs.comparison_config import OUTPUT_FOLDER
from configs.output_dir import get_output_folder


def get_filename_without_extension(file_path):
    """
    Extracts the file name without the extension from the given file path.
    """
    return os.path.splitext(os.path.basename(file_path))[0]

def replace_underscores_with_spaces(input_string):
    """
    Replaces all underscores in the given string with spaces.
    """
    result = input_string.replace("_", " ")
    result = result.replace("-", " ")
    return result

def save_graphs(plt, file_name):
    output_dir = get_output_folder()
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, f"{file_name}.jpg")

    plt.savefig(output_path)
    plt.close()