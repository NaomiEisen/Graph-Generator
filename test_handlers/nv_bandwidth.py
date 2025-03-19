import pandas as pd

from test_handlers.graphs_config import D2DMemcpyCeGraphConfig, DeviceAndHostGraphConfig
from data_structures.nv_bandwidth_struct import NvBandwidth
from data_structures.test import Test
from tests_config import NvBandwidthConfig
from graph_generators.bar_graph import plot_bar_graph
from utils.general import get_filename_without_extension

def device_and_host_memcpy_ce(nv_bandwith_struct):
    # Load test's data from file
    h2d_test = device_and_host_memcpy_ce_load_data(NvBandwidthConfig.H2D_MEMCPY_CE, nv_bandwith_struct)
    d2h_test = device_and_host_memcpy_ce_load_data(NvBandwidthConfig.D2H_MEMCPY_CE, nv_bandwith_struct)
    h2db_test = device_and_host_memcpy_ce_load_data(NvBandwidthConfig.H2DB_MEMCPY_CE, nv_bandwith_struct)
    d2hb_test = device_and_host_memcpy_ce_load_data(NvBandwidthConfig.D2HB_MEMCPY_CE, nv_bandwith_struct)

    tests_to_combine = [h2d_test, d2h_test, h2db_test, d2hb_test]
    combined_data = combine_data_frame(tests_to_combine)

    if combined_data.empty:
        return # Return if there is no data to plot
    
    # Append 'gpu' to each column name
    combined_data.columns = ['gpu ' + col for col in combined_data.columns]

    # TODO: delete 
    print(combined_data)

    # Create diagram
    plot_bar_graph(combined_data, DeviceAndHostGraphConfig, get_filename_without_extension(nv_bandwith_struct.org_file) + "d2h-and-h2d")

    # append to nv_bandwith_struct
    nv_bandwith_struct.add_test(Test(name= "device and host memcpy.ce", activate="true", data_pandas=combined_data))


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

def d2d_memcpy_ce(nv_bandwith_struct):
    # Load test's data from file
    d2d_read = d2d_load_data(NvBandwidthConfig.D2D_READ_MEMCPY_CE, nv_bandwith_struct)
    d2d_write = d2d_load_data(NvBandwidthConfig.D2D_WRITE_MEMCPY_CE, nv_bandwith_struct)
    d2d_read_bidirect = d2d_load_data(NvBandwidthConfig.D2D_READ_BIDIRECT_TOTAL_MEMCPY_CE, nv_bandwith_struct)
    d2d_write_bidirect = d2d_load_data(NvBandwidthConfig.D2D_WRITE_BIDIRECT_TOTAL_MEMCPY_CE, nv_bandwith_struct)

    tests_to_combine = [d2d_read, d2d_write, d2d_read_bidirect, d2d_write_bidirect]
    combined_data = combine_data_frame(tests_to_combine)

    if combined_data.empty:
        return # Return if there is no data to plot

    # Now combined_data will have all the rows stacked with their respective indices
    print(combined_data)

    # Create diagram
    plot_bar_graph(combined_data, D2DMemcpyCeGraphConfig, get_filename_without_extension(nv_bandwith_struct.org_file))

    # append to nv_bandwith_struct
    nv_bandwith_struct.add_test(Test(name= "device to device memcpy.ce", activate="true", data_pandas=combined_data))


def d2d_load_data(test_config, nv_bandwith_struct):
    # Check if the test is activated
    if test_config["activate"]:
        # Create the test from the configuration
        test = Test.test_from_config(test_config)
        
        # Parse the test data from the given file
        test.parse_test_data(nv_bandwith_struct.org_file)
        print(test.data_pandas)

         # Calculate the overall average for all values in the DataFrame, ignoring NaN values
        overall_avg = test.data_pandas.stack().mean()

        # Create a new DataFrame with 'overall_avg' as index and the average value as the column
        avg_df = pd.DataFrame({'average bandwidth (GB/s)': [overall_avg]}, index=[test.name])
        print(avg_df)

        test.data_pandas = avg_df
        # Return the DataFrame with the average value
        return test
    
    else:
        return None
    
def combine_data_frame(tests):
    # Filter out None values or empty data_pandas attributes
    valid_dfs = [test.data_pandas for test in tests if test is not None and test.data_pandas is not None and not test.data_pandas.empty]
    
    # Combine the DataFrames if there are any valid ones, else return an empty DataFrame
    return pd.concat(valid_dfs, axis=0) if valid_dfs else pd.DataFrame()

def start_nvbandwith(file):
    nv_bandwith_struct = NvBandwidth(org_file=file)

    # Process the device and host memcpy.ce tests
    device_and_host_memcpy_ce(nv_bandwith_struct)

    # Process the device to device mamcpy.ce
    d2d_memcpy_ce(nv_bandwith_struct)

    # all and host ce

    # same but sm


    # return the nvbandwith struct
