from data_structures.test import Test

class NvBandwidth:
    TYPE_ORG = 0
    TYPE_OPT = 1

    def __init__(self, org_file: str, tests=None, type_file=TYPE_ORG):
        """
        Initializes the NvBandwidth object with the given file and list of tests.
        """
        if tests is None:
            tests = []
        self.org_file = org_file
        self.Tests = tests
        self.type = type_file

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