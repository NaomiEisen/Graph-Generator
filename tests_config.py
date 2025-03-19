class NvBandwidthConfig:
    # memcpy_ce
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
        # DO NOT CHANGE - there are no title for the test
        "start": "SUM device_to_device_bidirectional_memcpy_read_ce_read2",  
        "end": "SUM device_to_device_bidirectional_memcpy_read_ce_total"       
    }

    D2D_WRITE_BIDIRECT_TOTAL_MEMCPY_CE = {
        "name": "d2d_bidirectional_memcpy_write_ce_total", 
        "activate": True,
        "offset": 3,
        # DO NOT CHANGE - there are no title for the test
        "start": "SUM device_to_device_bidirectional_memcpy_write_ce_write2",  
        "end": "SUM device_to_device_bidirectional_memcpy_write_ce_total"       
    }

    ALL2H_MEMCPY_CE = {
        "name": "all_to_host_memcpy_ce", 
        "activate": True,
        "offset": 2,
        "start": "Running all_to_host_memcpy_ce",  
        "end": "SUM all_to_host_memcpy_ce"       
    }

    ALL2H_BIDIRECT_MEMCPY_CE = {
        "name": "all_to_host_bidirectional_memcpy_ce", 
        "activate": True,
        "offset": 2,
        "start": "Running all_to_host_bidirectional_memcpy_ce",  
        "end": "SUM all_to_host_bidirectional_memcpy_ce"       
    }

    H2ALL_MAMCPY_CE = {
        "name": "host_to_all_memcpy_ce", 
        "activate": True,
        "offset": 2,
        "start": "Running host_to_all_memcpy_ce",  
        "end": "SUM host_to_all_memcpy_ce"  
    }

    H2ALL_BIDIRECT_MAMCPY_CE = {
        "name": "host_to_all_bidirectional_memcpy_ce", 
        "activate": True,
        "offset": 2,
        "start": "Running host_to_all_bidirectional_memcpy_ce",  
        "end": "SUM host_to_all_bidirectional_memcpy_ce"  
    }

    ALL2ONE_WRITE_CE = {
        "name": "all_to_one_write_ce", 
        "activate": True,
        "offset": 2,
        "start": "Running all_to_one_write_ce",  
        "end": "SUM all_to_one_write_ce"  
    }

    ALL2ONE_READ_CE = {
        "name": "all_to_one_read_ce", 
        "activate": True,
        "offset": 2,
        "start": "Running all_to_one_read_ce",  
        "end": "SUM all_to_one_read_ce"  
    }

    ONE2ALL_WRITE_CE = {
        "name": "one_to_all_write_ce", 
        "activate": True,
        "offset": 2,
        "start": "Running one_to_all_write_ce",  
        "end": "SUM one_to_all_write_ce"  
    }

    ONE2ALL_READ_CE = {
        "name": "one_to_all_read_ce", 
        "activate": True,
        "offset": 2,
        "start": "Running one_to_all_read_ce",  
        "end": "SUM one_to_all_read_ce"  
    }

    # memcpy_sm
    H2D_MEMCPY_SM = {
        "name": "host_to_device_memcpy_sm", 
        "activate": True,
        "offset": 2,
        "start": "Running host_to_device_memcpy_sm",  
        "end": "SUM host_to_device_memcpy_sm"       
    }

    D2H_MEMCPY_SM = {
        "name": "device_to_host_memcpy_sm", 
        "activate": True,
        "offset": 2,
        "start": "Running device_to_host_memcpy_sm",  
        "end": "SUM device_to_host_memcpy_sm"       
    }

    H2DB_MEMCPY_SM = {
        "name": "host_to_device_bidirectional_memcpy_sm", 
        "activate": True,
        "offset": 2,
        "start": "Running host_to_device_bidirectional_memcpy_sm",  
        "end": "SUM host_to_device_bidirectional_memcpy_sm"       
    }

    D2HB_MEMCPY_SM = {
        "name": "device_to_host_bidirectional_memcpy_sm", 
        "activate": True,
        "offset": 2,
        "start": "Running device_to_host_bidirectional_memcpy_sm",  
        "end": "SUM device_to_host_bidirectional_memcpy_sm "       
    }

    D2D_READ_MEMCPY_SM = {
        "name": "device_to_device_memcpy_read_sm", 
        "activate": True,
        "offset": 2,
        "start": "Running device_to_device_memcpy_read_sm",  
        "end": "SUM device_to_device_memcpy_read_sm"       
    }

    D2D_WRITE_MEMCPY_SM = {
        "name": "device_to_device_memcpy_write_sm", 
        "activate": True,
        "offset": 2,
        "start": "Running device_to_device_memcpy_write_sm",  
        "end": "SUM device_to_device_memcpy_write_sm"       
    }

    D2D_READ_BIDIRECT_TOTAL_MEMCPY_SM = {
        "name": "d2d_bidirectional_memcpy_read_sm_total", 
        "activate": True,
        "offset": 3,
        "start": "SUM device_to_device_bidirectional_memcpy_read_sm_read2",  
        "end": "SUM device_to_device_bidirectional_memcpy_read_sm_total"       
    }

    D2D_WRITE_BIDIRECT_TOTAL_MEMCPY_SM = {
        "name": "d2d_bidirectional_memcpy_write_sm_total", 
        "activate": True,
        "offset": 3,
        "start": "SUM device_to_device_bidirectional_memcpy_write_sm_write2",  
        "end": "SUM device_to_device_bidirectional_memcpy_write_sm_total"       
    }

    ALLD2H_MEMCPY_SM = {
        "name": "all_to_host_memcpy_sm", 
        "activate": True,
        "offset": 2,
        "start": "Running all_to_host_memcpy_sm",  
        "end": "SUM all_to_host_memcpy_sm"       
    }

    ALL2H_BIDIRECT_MEMCPY_SM = {
        "name": "all_to_host_bidirectional_memcpy_sm", 
        "activate": True,
        "offset": 2,
        "start": "Running all_to_host_bidirectional_memcpy_sm",  
        "end": "SUM all_to_host_bidirectional_memcpy_sm"       
    }

    H2ALL_MAMCPY_SM = {
        "name": "host_to_all_memcpy_sm", 
        "activate": True,
        "offset": 2,
        "start": "Running host_to_all_memcpy_sm",  
        "end": "SUM host_to_all_memcpy_sm"  
    }

    H2ALL_BIDIRECT_MAMCPY_SM = {
        "name": "host_to_all_bidirectional_memcpy_sm", 
        "activate": True,
        "offset": 2,
        "start": "Running host_to_all_bidirectional_memcpy_sm",  
        "end": "SUM host_to_all_bidirectional_memcpy_sm"  
    }

    ALL2ONE_WRITE_SM = {
        "name": "all_to_one_write_sm", 
        "activate": True,
        "offset": 2,
        "start": "Running all_to_one_write_sm",  
        "end": "SUM all_to_one_write_sm"  
    }

    ALL2ONE_READ_SM = {
        "name": "all_to_one_read_sm", 
        "activate": True,
        "offset": 2,
        "start": "Running all_to_one_read_sm",  
        "end": "SUM all_to_one_read_sm"  
    }

    ONE2ALL_WRITE_SM = {
        "name": "one_to_all_write_sm", 
        "activate": True,
        "offset": 2,
        "start": "Running one_to_all_write_sm",  
        "end": "SUM one_to_all_write_sm"  
    }

    ONE2ALL_READ_SM = {
        "name": "one_to_all_read_sm", 
        "activate": True,
        "offset": 2,
        "start": "Running one_to_all_read_sm",  
        "end": "SUM one_to_all_read_sm"  
    }
