from data_structures.test import Test

class NvBandwidth:
    def __init__(self, org_file: str, tests=None):
        """
        Initializes the NvBandwidth object with the given file and list of tests.
        """
        if tests is None:
            tests = []
        self.org_file = org_file
        self.Tests = tests

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