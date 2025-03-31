from data_structures.test import Test
from data_structures.test_verion import TestVersion


class NvBandwidth:

    def __init__(self, org_file: str, tests=None, file_version=TestVersion.V1):
        """
        Initializes the NvBandwidth object with the given file and list of tests.
        """
        if tests is None:
            tests = []
        self.org_file = org_file
        self.Tests = tests
        self.version = file_version

    def add_test(self, test: Test):
        """
        Adds a Test object to the Tests array.
        """
        self.Tests.append(test)

    def get_tests(self):
        """
        Returns the list of Test objects.
        """
        return self.Tests