from data_structures.test import Test
from utils.set_users_args import determine_version


class NvBandwidth:
    def __init__(self, org_file: str, tests=None):
        """
        Initializes the NvBandwidth object with the given file and list of tests.
        """
        if tests is None:
            tests = []
        self.org_file = org_file
        self.test_list = tests
        self.version = determine_version(org_file)

    def add_test(self, test: Test):
        """
        Adds a Test object to the Tests array.
        """
        self.test_list.append(test)

    def get_tests(self):
        """
        Returns the list of Test objects.
        """
        return self.test_list