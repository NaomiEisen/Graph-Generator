from utils.set_users_args import determine_version


class AllReduce:
    def __init__(self, org_file: str, test = None):
        self.org_file = org_file
        self.Test = test
        self.version = determine_version(org_file)

    # def add_test(self, test: Test):
    #     self.Test = test
    #
    # def get_test(self):
    #     return self.Test