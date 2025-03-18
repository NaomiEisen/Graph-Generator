import pandas as pd
import matplotlib.pyplot as plt

from helpers.handle_data import load_data_matrix_format

class Test:
    def __init__(self, name: str, activate: bool, start_indicator: str, end_indicator: str, offset: int, data_pandas=None):
        """
        Initializes the Test object with the given attributes.
        
        :param name: Name of the test
        :param activate: Flag indicating if the test is active or not
        :param start_indicator: The text indicating the start of the test range
        :param end_indicator: The text indicating the end of the test range
        :param offset: Number of lines to shift the start index forward
        :param data_pandas: Optional Pandas DataFrame holding the test data (defaults to None)
        """
        self.name = name
        self.activate = activate
        self.start_indicator = start_indicator
        self.end_indicator = end_indicator
        self.offset = offset
        self.data_pandas = data_pandas

    def parse_test_data(self, file: str):
        """
        Parses the test data from the given file by finding the start and end indices.
        
        :param file: The file path to parse
        :return: None (Calls load_data with the indexes)
        """
        start_index = None
        end_index = None

        # Open the file and search for the start and end indicators
        with open(file, 'r') as f:
            lines = f.readlines()
            for i, line in enumerate(lines):
                if self.start_indicator in line and start_index is None:
                    start_index = i + self.offset # Apply offset
                if self.end_indicator in line and start_index is not None:
                    end_index = i
                    break

        # Check if both start and end indices were found
        if start_index is not None and end_index is not None:
            # Call the load_data function with the file and indexes
            print(start_index)
            print(end_index)
            load_data_matrix_format(file, start_index, end_index, 1)
        else:
            raise ValueError("Could not find both start and end indicators in the file.")



    def get_test_data(self, data_pandas: pd.DataFrame):
        """
        Returns the portion of the data based on the start and end indicators, with offset applied.
        
        :param data_pandas: The pandas DataFrame holding the test data
        :return: A subset of the pandas DataFrame corresponding to the test range
        """
        # Ensure data_pandas is provided
        if data_pandas is None:
            raise ValueError("Data must be provided to get the test data.")
        
        # Find the start and end indices based on the start and end indicators
        start_index = data_pandas[data_pandas['column_name'].str.contains(self.start_indicator)].index[0] + self.offset
        end_index = data_pandas[data_pandas['column_name'].str.contains(self.end_indicator)].index[0]
        
        # Extract the data slice based on the indices
        test_data = data_pandas.iloc[start_index:end_index + 1]
        return test_data

    def create_graph(self, data_pandas: pd.DataFrame):
        """
        Creates a graph based on the test data (e.g., a line graph).
        
        :param data_pandas: The pandas DataFrame holding the test data
        :return: None (Displays the graph)
        """
        pass

    def __str__(self):
        """
        String representation of the Test object that includes all its attributes.
        """
        return f"Test(name={self.name}, activate={self.activate}, start_indicator={self.start_indicator}, " \
               f"end_indicator={self.end_indicator}, offset={self.offset}, data_pandas={self.data_pandas})"

    @classmethod
    def test_from_config(cls, config: dict, data_pandas=None):
        """
        Class method to initialize a Test object from the NvBandwidthConfig dictionary.

        :param config: The configuration dictionary containing the test attributes
        :param data_pandas: Optional Pandas DataFrame (defaults to None)
        :return: An instance of the Test class
        """
        return cls(
            name=config["name"],
            activate=config["activate"],
            start_indicator=config["start"],
            end_indicator=config["end"],
            offset=config["offset"],
            data_pandas=data_pandas
        )