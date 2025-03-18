from data_structues.nv_bandwidth_struct import NvBandwidth
from data_structues.test import Test
from tests_config import NvBandwidthConfig
import pandas as pd


def device_and_host_memcpy_ce(nv_bandwith_struct: NvBandwidth):
    # Load test's data from file
    h2d_test = device_and_host_memcpy_ce_load_data(NvBandwidthConfig.H2D_MEMCPY_CE, nv_bandwith_struct)
    d2h_test = device_and_host_memcpy_ce_load_data(NvBandwidthConfig.D2H_MEMCPY_CE, nv_bandwith_struct)
    h2db_test = device_and_host_memcpy_ce_load_data(NvBandwidthConfig.H2DB_MEMCPY_CE, nv_bandwith_struct)
    d2hb_test = device_and_host_memcpy_ce_load_data(NvBandwidthConfig.D2HB_MEMCPY_CE, nv_bandwith_struct)

    # Combine the individual DataFrames into a single DataFrame
    combined_data = pd.concat([
        h2d_test.data_pandas, 
        d2h_test.data_pandas, 
        h2db_test.data_pandas, 
        d2hb_test.data_pandas
    ], axis=0)

    # Now combined_data will have all the rows stacked with their respective indices
    print(combined_data)

    # append to  nv_bandwith_struct

    # Create diagram


    


def device_and_host_memcpy_ce_load_data(test_config, nv_bandwith_struct):
    # Check if the test is activated
    if test_config["activate"]:
        # Create the test from the configuration
        test = Test.test_from_config(test_config)
        
        # Parse the test data from the given file
        test.parse_test_data(nv_bandwith_struct.org_file)
        
        # Set the custom index for the data
        test.data_pandas.index = [test_config["name"]]  # Set custom index from the config
        
        # Print the result
        print(test.data_pandas)

        return test
    
    else:
        return None

    


    # append to tests

def start_nvbandwith(file):
    nv_bandwith_struct = NvBandwidth(org_file=file)

    # Process the device and host memcpy tests
    device_and_host_memcpy_ce(nv_bandwith_struct)
    print("after")

    # device and host ce

    # device to device ce

    # all and host ce

    # same but sm


    # return the nvbandwith struct
