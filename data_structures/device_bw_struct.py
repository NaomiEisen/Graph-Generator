from data_structures.test import Test

class DeviceBw:
    def __init__(self, org_file: str, test=None):
        """
        Initializes the NvBandwidth object with the given file and list of tests.
        
        :param org_file: The original file path associated with the bandwidth tests
        :param tests: List of Test objects (defaults to an empty list)
        """
        self.org_file = org_file
        self.Test = test

    def add_test(self, test: Test):
        """
        Adds a Test object to the Tests array.

        :param test: Test object to be added
        """
        self.Test = test

    def get_tests(self):
        """
        Returns the list of Test objects.

        :return: List of Test objects
        """
        return self.Test