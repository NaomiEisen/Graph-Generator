import os

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
