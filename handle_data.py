import pandas as pd
import matplotlib.pyplot as plt
import os

def load_data_matrix_format(file_name):
    """
    Loads data from a .txt or Excel file into a Pandas DataFrame.
    """
    try:
        if file_name.endswith((".xls", ".xlsx")):
            data = pd.read_excel(file_name, engine="openpyxl")  # Use openpyxl for modern Excel files
        else:
            data = pd.read_csv(file_name, sep=r'\s+', header=0, skipinitialspace=True)  

        return data
    except FileNotFoundError as e:  # Invalid file name or unavailable file
        print(f"Error: The file '{file_name}' was not found.")
        raise e
    except pd.errors.EmptyDataError as e:  # File available but empty
        print("Error: The file is empty.")
        raise e
    except pd.errors.ParserError as e:  # File format issue
        print("Error: The file could not be parsed.")
        raise e
    except Exception as e:  # Other errors
        print("Error: An unexpected error occurred while loading the file.")
        raise e
    
def get_files_list(args):
    # If any input in the list is a directory, get all files inside
    files = []
    for file in args:
        if isinstance(file, str) and os.path.isdir(file):
            # Append only valid file paths from the directory
            files.extend(
                os.path.join(file, f) for f in os.listdir(file) if os.path.isfile(os.path.join(file, f))
            )
        else:
            # If it's already a file, keep it
            files.append(file)

    return files

def save_graphs(plt, file_name_without_extension):
    output_dir = "output-graphs"
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, f"{file_name_without_extension}_output.jpg")

    #plt.show()
    plt.savefig(output_path)
    plt.close()