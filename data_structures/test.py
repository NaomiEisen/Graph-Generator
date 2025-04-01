class Test:
    def __init__(self, name, activate, start_indicator =  None, end_indicator = None, offset = 0, data_pandas=None):
        """
        Initializes the Test object with the given attributes.
        """
        self.name = name
        self.activate = activate
        self.start_indicator = start_indicator
        self.end_indicator = end_indicator
        self.offset_from_start = offset
        self.data_pandas = data_pandas

    def parse_test_data(self, file, offset_to_right, func):
        """
        Parses the test data from the given file by finding the start and end indices.
        """
        start_index = None
        end_index = None

        # Open the file and search for the start and end indicators
        with open(file, 'r') as f:
            lines = f.readlines()

            if self.end_indicator == "":
                end_index = len(lines)

            for i, line in enumerate(lines):
                if self.start_indicator in line and start_index is None:
                    start_index = i + self.offset_from_start # Apply offset
                if self.end_indicator in line and start_index is not None and end_index is None:
                    end_index = i
                    break

        # Check if both start and end indices were found
        if start_index is not None and end_index is not None:
            # Call the load_data function with the file and indexes
            self.data_pandas = func(file, start_index, end_index, offset_to_right)
        else:
            #raise Exception("Could not find both start and end indicators in the file.")
            self.data_pandas = None


    @classmethod
    def test_from_config(cls, config: dict, data_pandas=None):
        """
        Class method to initialize a Test object from the NvBandwidthConfig dictionary.

        Args:
            config: The configuration dictionary containing the test attributes
            data_pandas: Optional Pandas DataFrame (defaults to None)
        Returns:
            An instance of the Test class
        """
        return cls(
            name=config["name"],
            activate=config["activate"],
            start_indicator=config["start"],
            end_indicator=config["end"],
            offset=config["offset"],
            data_pandas=data_pandas
        )


    # TODO: maybe delete later
    def __str__(self):
        """
        String representation of the Test object that includes all its attributes. For debug purposes
        """
        return f"Test(name={self.name}, activate={self.activate}, start_indicator={self.start_indicator}, " \
               f"end_indicator={self.end_indicator}, offset={self.offset_from_start}, data_pandas={self.data_pandas})"