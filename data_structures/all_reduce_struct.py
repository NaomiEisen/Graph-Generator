from data_structures.test import Test

class AllReduce:
    TYPE_V1 = 0
    TYPE_V2 = 1

    def __init__(self, org_file: str, test = None, file_version=TYPE_V1):
        """
        Initializes the NvBandwidth object with the given file and list of tests.
        """
        self.org_file = org_file
        self.Test = test
        self.version = file_version

    def add_test(self, test: Test):
        """
        Adds a Test object to the Tests array.
        """
        self.Test = test

    def get_test(self):
        """
        Returns the list of Test objects.
        """
        return self.Test