class NvBandwidthConfig:
    # Define the configuration for the tests
    # single gpu eith host memcpy_ce
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

    # device to device memcpy_ce
    # device to device memcpy_read_ce
    D2D_READ_MEMCPY_CE = {
        "name": "d2d_memcpy_read_ce", 
        "activate": True,
        "offset": 2,
        "start": "Running device_to_device_memcpy_read_ce",  
        "end": "SUM device_to_device_memcpy_read_ce"       
    }

    # device to device memcpy_write_ce
    D2D_WRITE_MEMCPY_CE = {
        "name": "d2d_memcpy_write_ce", 
        "activate": True,
        "offset": 2,
        "start": "Running device_to_device_memcpy_write_ce",  
        "end": "SUM device_to_device_memcpy_write_ce"       
    }

    D2D_READ_BIDIRECT_TOTAL_MEMCPY_CE = {
        "name": "d2d_bidirectional_memcpy_read_ce_total", 
        "activate": True,
        "offset": 3,
        "start": "SUM device_to_device_bidirectional_memcpy_read_ce_read2",  
        "end": "SUM device_to_device_bidirectional_memcpy_read_ce_total"       
    }

    D2D_WRITE_BIDIRECT_TOTAL_MEMCPY_CE = {
        "name": "d2d_bidirectional_memcpy_write_ce_total", 
        "activate": True,
        "offset": 3,
        "start": "SUM device_to_device_bidirectional_memcpy_write_ce_write2",  
        "end": "SUM device_to_device_bidirectional_memcpy_write_ce_total"       
    }
