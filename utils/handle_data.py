import pandas as pd

def load_data_two_column(file_name, start_index=0, end_index=None, right_offset=0):
    try:
        with open(file_name, "r") as file:
            lines = file.readlines()

        if end_index is None:
            end_index = len(lines)

        # Extract header from the first line
        header_line = lines[start_index].strip()
        header_parts = header_line.rsplit(maxsplit=1)
        header = [" ".join(header_parts[:-1]), header_parts[-1]]

        # Extract data lines
        data_lines = [line.strip().split(maxsplit=1) for line in lines[start_index + 1:end_index] if line.strip()]

        # Create DataFrame from data
        data = pd.DataFrame(data_lines, columns=header)

        data = data.apply(pd.to_numeric, errors='coerce')

        return data

    # Handle errors
    except FileNotFoundError as e:
        print(f"Error: The file '{file_name}' was not found.")
        raise e
    except Exception as e:
        print(f"Error: An unexpected error occurred while loading the file: {e}")
        raise e


def load_data_matrix_format(file_name, start_index=0, end_index=None, offset_right=0):
    """
    Loads data from a .txt or Excel file into a Pandas DataFrame within the specified range of lines.
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

            # Convert data to numeric format, non numeric values will ce converted to NaN
            data = data.apply(pd.to_numeric, errors='coerce')

        return data

    # Handle errors
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
    
    

    
