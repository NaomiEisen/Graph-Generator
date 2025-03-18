import pandas as pd
import matplotlib.pyplot as plt
import os


def load_data_matrix_format(file_name, start_index=0, end_index=None, offset_right=0):
    """
    Loads data from a .txt or Excel file into a Pandas DataFrame within the specified range of lines.

    :param file_name: The path to the file to load.
    :param start_index: The starting line index for loading data (inclusive).
    :param end_index: The ending line index for loading data (inclusive).
    :param offset_right: Number of values to remove from the beginning of each row (excluding the header).
    :return: A pandas DataFrame with the data loaded in the specified range.
    """
    try:
        if file_name.endswith((".xls", ".xlsx")):
            data = pd.read_excel(file_name, engine="openpyxl")  # Use openpyxl for modern Excel files
        else:
            with open(file_name, "r") as f:
                lines = f.readlines()

            # Extract only the required lines based on start_index and end_index
            if end_index is None:
                end_index = len(lines) - 1

            selected_lines = lines[start_index:end_index]

            # Extract header from the first selected line
            header = selected_lines[0].strip().split()

            # Extract data (excluding header)
            data_lines = [line.strip().split() for line in selected_lines[1:] if line.strip()]

            # Apply offset_right: Remove the first `offset_right` elements from each row
            if offset_right > 0:
                data_lines = [row[offset_right:] for row in data_lines]

            # Convert processed data back to a pandas DataFrame
            data = pd.DataFrame(data_lines, columns=header)

            # Convert data to numeric format, coercing errors to NaN
            data = data.apply(pd.to_numeric, errors='coerce')

        return data

    except FileNotFoundError as e:
        print(f"Error: The file '{file_name}' was not found.")
        raise e
    except pd.errors.EmptyDataError as e:
        print("Error: The file is empty.")
        raise e
    except pd.errors.ParserError as e:
        print("Error: The file could not be parsed.")
        raise e
    except Exception as e:
        print(f"Error: An unexpected error occurred while loading the file: {e}")
        raise e



# def load_data_matrix_format(file_name):
#     """
#     Loads data from a .txt or Excel file into a Pandas DataFrame.
#     """
#     try:
#         if file_name.endswith((".xls", ".xlsx")):
#             data = pd.read_excel(file_name, engine="openpyxl")  # Use openpyxl for modern Excel files
#         else:
#             data = pd.read_csv(file_name, sep=r'\s+', header=0, skipinitialspace=True)  

#         return data
#     except FileNotFoundError as e:  # Invalid file name or unavailable file
#         print(f"Error: The file '{file_name}' was not found.")
#         raise e
#     except pd.errors.EmptyDataError as e:  # File available but empty
#         print("Error: The file is empty.")
#         raise e
#     except pd.errors.ParserError as e:  # File format issue
#         print("Error: The file could not be parsed.")
#         raise e
#     except Exception as e:  # Other errors
#         print("Error: An unexpected error occurred while loading the file.")
#         raise e
    
    
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
    
def save_graphs(plt, file_name_without_extension):
    output_dir = "output-graphs"
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, f"{file_name_without_extension}_output.jpg")

    #plt.show()
    plt.savefig(output_path)
    plt.close()