class NvBandwidthConfig:
    # Define the configuration for the tests, including missing attributes
    H2D_MEMCPY_CE = {
        "name": "host_to_device_memcpy_ce", 
        "activate": True,
        "offset": 2,
        "start": "Running host_to_device_memcpy_ce",  
        "end": "SUM host_to_device_memcpy_ce"       
    }

    D2H_MEMCPY_CE = {
        "name": "device_to_host_memcpy_ce", 
        "activate": True,
        "offset": 2,
        "start": "Running device_to_host_memcpy_ce",  
        "end": "SUM device_to_host_memcpy_ce"       
    }

    H2DB_MEMCPY_CE = {
        "name": "host_to_device_bidirectional_memcpy_ce", 
        "activate": True,
        "offset": 2,
        "start": "Running host_to_device_bidirectional_memcpy_ce",  
        "end": "SUM host_to_device_bidirectional_memcpy_ce"       
    }

    D2HB_MEMCPY_CE = {
        "name": "device_to_host_bidirectional_memcpy_ce", 
        "activate": True,
        "offset": 2,
        "start": "Running device_to_host_bidirectional_memcpy_ce",  
        "end": "SUM device_to_host_bidirectional_memcpy_ce "       
    }

    # device to device memcpy.ce
    D2D_READ_MEMCPY_CE = {
        "name": "device_to_device_memcpy_read_ce", 
        "activate": True,
        "offset": 0,
        "start": "start_indicator",  
        "end": "end_indicator"       
    }

# Example usage:
# print(NvBandwidthConfig.H2D_MEMCPY_CE)
# print(NvBandwidthConfig.D2H_MEMCPY_CE)

# test_name = NvBandwidthConfig.H2D_MEMCPY_CE["name"]
# test_activate = NvBandwidthConfig.H2D_MEMCPY_CE["activate"]
# test_offset = NvBandwidthConfig.H2D_MEMCPY_CE["offset"]

