import os

def get_filename_without_extension(file_path):
    """
    Extracts the file name without the extension from the given file path.
    """
    return os.path.splitext(os.path.basename(file_path))[0]