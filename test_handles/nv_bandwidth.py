import pandas as pd
from matplotlib import pyplot as plt

from globals import ColorPalette, Const
from data_structues.nv_bandwidth_struct import NvBandwidth
from data_structues.test import Test
from tests_config import NvBandwidthConfig
from graph_generators.bar_graph import plot_bar_graph

class DeviceAndHostGraphConfig:
    TITLE = 'memcpy between host and devices'
    X_AXIS = 'test name'
    Y_AXIS = 'bandwidth (GB/s)'
    COLOR_THEME = ColorPalette.SUNSET_THEME
    BAR_WIDTH = 0.8

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
    plot_bar_graph(combined_data)


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

def plot_bar_graph(data):
    """
    Plots a bar graph for the combined data with 4 sections, each representing a row.
    Each section will have 8 bars, one for each column.
    
    :param combined_data: The Pandas DataFrame containing the combined data.
    """
    # Ensure all data is numeric (convert non-numeric values to NaN and handle them)
    #data = data.apply(pd.to_numeric, errors='coerce')

    # Drop rows or columns with NaN values if needed
    data = data.dropna(axis=1, how='all')  # Drop columns with all NaN values
    data = data.dropna(axis=0, how='all')  # Drop rows with all NaN values

    # Set the figure size using constants from Const class
    plt.figure(figsize=(Const.WIDTH, Const.HEIGHT))

    # Create the bar plot with colors from the GIRLY_THEME
    ax = data.plot(kind='bar', width=DeviceAndHostGraphConfig.BAR_WIDTH, color=DeviceAndHostGraphConfig.COLOR_THEME)

    # Set plot title and labels
    plt.title(DeviceAndHostGraphConfig.TITLE, fontsize=14)
    plt.xlabel(DeviceAndHostGraphConfig.X_AXIS, fontsize=12)
    plt.ylabel(DeviceAndHostGraphConfig.Y_AXIS, fontsize=12)

    # Rotate x-axis labels for better readability
    plt.xticks(rotation=45, ha='right')

    # Adjust layout to make sure everything fits well
    plt.tight_layout()

    # Display the graph
    plt.show()



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
