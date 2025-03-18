from data_structues.nv_bandwidth_struct import NvBandwidth
from data_structues.test import Test
from tests_config import NvBandwidthConfig


def device_and_host_memcpy_ce(nv_bandwith_struct: NvBandwidth):
    print("got here")
    h2d_test = Test.test_from_config(NvBandwidthConfig.H2D_MEMCPY_CE)
    print(h2d_test)


    h2d_test.parse_test_data(nv_bandwith_struct.org_file)
    print(h2d_test.data_pandas)
    # d2h_test = Test.test_from_config(NvBandwidthConfig.D2H_MEMCPY_CE)
    # h2db_test = Test.test_from_config(NvBandwidthConfig.D2HB_MEMCPY_CE)
    # h2db_test = Test.test_from_config(NvBandwidthConfig.H2DB_MEMCPY_CE)

    # create one test struct from this

    # append to tests

def start_nvbandwith(file):
    nv_bandwith_struct = NvBandwidth(org_file=file)
    print(nv_bandwith_struct)

    # Call the function to process the device and host memcpy tests
    device_and_host_memcpy_ce(nv_bandwith_struct)
    print("after")
    #  -- create all the test struct
    # device and host ce

    # device to device ce

    # all and host ce

    # same but sm


    # return the nvbandwith struct
