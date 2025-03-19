from collections import defaultdict
import inspect
import pandas as pd

from graphs_config import AvgValueBarGraphConfig, AllGpusBarGraphConfig
from data_structures.nv_bandwidth_struct import NvBandwidth
from data_structures.test import Test
from tests_config import NvBandwidthConfig
from graph_generators.bar_graph import plot_bar_graph
from utils.general import get_filename_without_extension



def combined_test_from_separated_rows(nv_bandwith_struct, configs, final_name, test_name):
    """
    Loads test data for multiple configurations, combines them into a single DataFrame,
    modifies column names, and generates a bar graph.

    :param nv_bandwith_struct: The structure containing bandwidth test information.
    :param configs: A list of configurations to load and combine.
    :param final_name: The name to use for the output graph and test entry.
    """
    # Load and combine test data
    tests_to_combine = [load_data_and_append_name_index(config, nv_bandwith_struct) for config in configs]
    combined_data = combine_data_frame(tests_to_combine)

    if combined_data.empty:
        return  # Return if there is no data to process

    # Append 'gpu' to each column name
    combined_data.columns = ['GPU ' + col for col in combined_data.columns]

    # Debugging print (remove later if not needed)
    print(combined_data)

    # Create bar graph
    plot_bar_graph(combined_data, AllGpusBarGraphConfig, get_filename_without_extension(nv_bandwith_struct.org_file) + final_name, test_name)

    # Append results to nv_bandwith_struct
    nv_bandwith_struct.add_test(Test(name=final_name, activate="true", data_pandas=combined_data))


def combined_test_from_separated_mat(nv_bandwith_struct, configs, final_name, test_name):
    """
    Loads test data for multiple configurations, combines them into a single DataFrame,
    and generates a bar graph.

    :param nv_bandwith_struct: The structure containing bandwidth test information.
    :param configs: A list of configurations to load and combine.
    :param final_name: The name to use for the output graph and test entry.
    """
    # Load and combine test data
    tests_to_combine = [load_mat_data_to_avg(config, nv_bandwith_struct) for config in configs]
    combined_data = combine_data_frame(tests_to_combine)

    if combined_data.empty:
        return  # Return if there is no data to process

    # Debugging print (remove later if not needed)
    print(combined_data)

    # Create bar graph
    plot_bar_graph(combined_data, AvgValueBarGraphConfig, get_filename_without_extension(nv_bandwith_struct.org_file) + final_name, test_name)
    
    # Append results to nv_bandwith_struct
    nv_bandwith_struct.add_test(Test(name=final_name, activate="true", data_pandas=combined_data))


def device_to_device_memcpy_ce(nv_bandwith_struct):
    # Load test's data from file
    d2d_read = load_mat_data_to_avg(NvBandwidthConfig.D2D_READ_MEMCPY_CE, nv_bandwith_struct)
    d2d_write = load_mat_data_to_avg(NvBandwidthConfig.D2D_WRITE_MEMCPY_CE, nv_bandwith_struct)
    d2d_read_bidirect = load_mat_data_to_avg(NvBandwidthConfig.D2D_READ_BIDIRECT_TOTAL_MEMCPY_CE, nv_bandwith_struct)
    d2d_write_bidirect = load_mat_data_to_avg(NvBandwidthConfig.D2D_WRITE_BIDIRECT_TOTAL_MEMCPY_CE, nv_bandwith_struct)

    tests_to_combine = [d2d_read, d2d_write, d2d_read_bidirect, d2d_write_bidirect]
    combined_data = combine_data_frame(tests_to_combine)

    if combined_data.empty:
        return # Return if there is no data to plot

    # Now combined_data will have all the rows stacked with their respective indices
    print(combined_data)

    # Create diagram
    plot_bar_graph(combined_data, AvgValueBarGraphConfig, get_filename_without_extension(nv_bandwith_struct.org_file))

    # append to nv_bandwith_struct
    nv_bandwith_struct.add_test(Test(name= "device to device memcpy.ce", activate="true", data_pandas=combined_data))
    

def load_data_and_append_name_index(test_config, nv_bandwith_struct):
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
    

def load_mat_data_to_avg(test_config, nv_bandwith_struct):
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

def group_nv_bandwidth_configs():
    grouped_configs = defaultdict(list)

    # Get all class attributes
    for name, value in inspect.getmembers(NvBandwidthConfig):
        # Ensure it's a dictionary and has 'group_id'
        if isinstance(value, dict) and 'group_id' in value:
            grouped_configs[value['group_id']].append(value)

    # Convert to list of lists
    return list(grouped_configs.values())


def start_nvbandwith(file):
    nv_bandwith_struct = NvBandwidth(org_file=file)

    grouped_test_configs = group_nv_bandwidth_configs()
    for config_group in grouped_test_configs:
        group_id = config_group[0]['group_id']  # Get group_id from the first config in the group
        group_info = NvBandwidthConfig.GROUPS_INFO[group_id]  # Lookup group info

        if group_info['group_type'] == NvBandwidthConfig.GROUP_FROM_ROWS:
            combined_test_from_separated_rows(nv_bandwith_struct, config_group, group_info["file_name"], group_info["test_name"])
        elif group_info['group_type'] == NvBandwidthConfig.GROUP_FROM_MAT:
            combined_test_from_separated_mat(nv_bandwith_struct, config_group, group_info["file_name"], group_info["test_name"])

    # #  -- Process ce tests --
    # # device <-> host memcpy.ce tests
    # configs_d_and_h_ce = [
    # NvBandwidthConfig.H2D_MEMCPY_CE,
    # NvBandwidthConfig.D2H_MEMCPY_CE,
    # NvBandwidthConfig.H2DB_MEMCPY_CE,
    # NvBandwidthConfig.D2HB_MEMCPY_CE
    # ]
    # combined_test_from_separated_rows(nv_bandwith_struct, configs_d_and_h_ce, "d2h_and_h2d_ce_old")

    # # device to device mamcpy.ce
    # configs_d2d_ce = [
    # NvBandwidthConfig.D2D_READ_MEMCPY_CE,
    # NvBandwidthConfig.D2D_WRITE_MEMCPY_CE,
    # NvBandwidthConfig.D2D_READ_BIDIRECT_TOTAL_MEMCPY_CE,
    # NvBandwidthConfig.D2D_WRITE_BIDIRECT_TOTAL_MEMCPY_CE
    # ]
    # combined_test_from_separated_mat(nv_bandwith_struct, configs_d2d_ce, "d2d_ce_old")

    # # all <-> host ce
    # configs_all_and_host_ce = [
    # NvBandwidthConfig.H2ALL_MAMCPY_CE,
    # NvBandwidthConfig.H2ALL_BIDIRECT_MAMCPY_CE,
    # NvBandwidthConfig.ALL2H_MEMCPY_CE,
    # NvBandwidthConfig.ALL2H_BIDIRECT_MEMCPY_CE
    # ]
    # combined_test_from_separated_rows(nv_bandwith_struct, configs_all_and_host_ce, "all2h_and_h2all_ce_old")
    # #all_and_host_memcpy_ce(nv_bandwith_struct)

    # # all <-> one ce
    # configs_all_and_one_ce = [
    # NvBandwidthConfig.ALL2ONE_READ_CE,
    # NvBandwidthConfig.ALL2ONE_WRITE_CE,
    # NvBandwidthConfig.ONE2ALL_READ_CE,
    # NvBandwidthConfig.ONE2ALL_WRITE_CE
    # ]
    # combined_test_from_separated_rows(nv_bandwith_struct, configs_all_and_one_ce, "all2one_and_one2all_ce_old")

    # #  -- Process sm tests --
    # # device <-> host memcpy.sm tests
    # configs_d_and_h_sm = [
    # NvBandwidthConfig.H2D_MEMCPY_SM,
    # NvBandwidthConfig.D2H_MEMCPY_SM,
    # NvBandwidthConfig.H2DB_MEMCPY_SM,
    # NvBandwidthConfig.D2HB_MEMCPY_SM
    # ]
    # combined_test_from_separated_rows(nv_bandwith_struct, configs_d_and_h_sm, "d2h_and_h2d_sm_old")

    # # device to device mamcpy.ce
    # configs_d2d_sm = [
    # NvBandwidthConfig.D2D_READ_MEMCPY_SM,
    # NvBandwidthConfig.D2D_WRITE_MEMCPY_SM,
    # NvBandwidthConfig.D2D_READ_BIDIRECT_TOTAL_MEMCPY_SM,
    # NvBandwidthConfig.D2D_WRITE_BIDIRECT_TOTAL_MEMCPY_SM
    # ]
    # #device_to_device_memcpy_ce(nv_bandwith_struct)
    # combined_test_from_separated_mat(nv_bandwith_struct, configs_d2d_sm, "d2d_sm_old")

    # # all <-> host ce
    # configs_all_and_host_sm = [
    # NvBandwidthConfig.H2ALL_MAMCPY_SM,
    # NvBandwidthConfig.H2ALL_BIDIRECT_MAMCPY_SM,
    # NvBandwidthConfig.ALL2H_MEMCPY_SM,
    # NvBandwidthConfig.ALL2H_BIDIRECT_MEMCPY_SM
    # ]
    # combined_test_from_separated_rows(nv_bandwith_struct, configs_all_and_host_sm, "all2h_and_h2all_sm_old")
    # #all_and_host_memcpy_ce(nv_bandwith_struct)

    # # all <-> one ce
    # configs_all_and_one_sm = [
    # NvBandwidthConfig.ALL2ONE_READ_SM,
    # NvBandwidthConfig.ALL2ONE_WRITE_SM,
    # NvBandwidthConfig.ONE2ALL_READ_SM,
    # NvBandwidthConfig.ONE2ALL_WRITE_SM
    # ]
    # combined_test_from_separated_rows(nv_bandwith_struct, configs_all_and_one_sm, "all2one_and_one2all_sm_old")


    # return the nvbandwith struct
