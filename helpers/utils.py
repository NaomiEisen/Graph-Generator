import os

def get_filename_without_extension(file_path):
    """
    Extracts the file name without the extension from the given file path.

    :param file_path: The full path to the file.
    :return: The file name without the extension.
    """
    return os.path.splitext(os.path.basename(file_path))[0]