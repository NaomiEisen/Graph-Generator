from data_structures.test import Test
from data_structures.test_verion import TestVersion

class AllReduce:
    def __init__(self, org_file: str, test = None, file_version=TestVersion.V1):
        """
        Initializes the NvBandwidth object with the given file and optional Test object.
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