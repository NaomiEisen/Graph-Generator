class NvBandwidthConfig:

    # Group version 1
    GROUPS_INFO = {
        1: {"file_name": "D2D_read_write_ce", "test_name": "Device To Device Read&Write memcpy_ce"},
        2: {"file_name": "D2D_read_write_sm", "test_name": "Device To Device Read&Write memcpy_sm"},
    }

    # Tests configs
    # -- memcpy ce
    H2D_MEMCPY_CE = {
        "name": "host_to_device_memcpy_ce", 
        "activate": True,
        "offset": 2,
        "right_offset": 1,
        "start": "Running host_to_device_memcpy_ce",  
        "end": "SUM host_to_device_memcpy_ce",
        "group_id": 3
    }

    D2H_MEMCPY_CE = {
        "name": "device_to_host_memcpy_ce", 
        "activate": True,
        "offset": 2,
        "right_offset": 1,
        "start": "Running device_to_host_memcpy_ce",  
        "end": "SUM device_to_host_memcpy_ce",
        "group_id": 4
    }

    H2DB_MEMCPY_CE = {
        "name": "host_to_device_bidirectional_memcpy_ce", 
        "activate": True,
        "offset": 2,
        "right_offset": 1,
        "start": "Running host_to_device_bidirectional_memcpy_ce",  
        "end": "SUM host_to_device_bidirectional_memcpy_ce",
        "group_id": 5
    }

    D2HB_MEMCPY_CE = {
        "name": "device_to_host_bidirectional_memcpy_ce", 
        "activate": True,
        "offset": 2,
        "right_offset": 1,
        "start": "Running device_to_host_bidirectional_memcpy_ce",  
        "end": "SUM device_to_host_bidirectional_memcpy_ce ",
        "group_id": 6
    }

    D2D_READ_MEMCPY_CE = {
        "name": "d2d_memcpy_read_ce",
        "activate": True,
        "offset": 2,
        "right_offset": 1,
        "start": "Running device_to_device_memcpy_read_ce",
        "end": "SUM device_to_device_memcpy_read_ce",
        "group_id": 1
    }

    D2D_WRITE_MEMCPY_CE = {
        "name": "d2d_memcpy_write_ce",
        "activate": True,
        "offset": 2,
        "right_offset": 1,
        "start": "Running device_to_device_memcpy_write_ce",
        "end": "SUM device_to_device_memcpy_write_ce",
        "group_id": 1
    }

    D2D_READ_BIDIRECT_TOTAL_MEMCPY_CE = {
        "name": "d2d_bidirectional_memcpy_read_ce_total",
        "activate": True,
        "offset": 3,
        "right_offset": 1,
        # DO NOT CHANGE - there is no title for the test
        "start": "SUM device_to_device_bidirectional_memcpy_read_ce_read2",
        "end": "SUM device_to_device_bidirectional_memcpy_read_ce_total",
        "group_id": 1
    }

    D2D_WRITE_BIDIRECT_TOTAL_MEMCPY_CE = {
        "name": "d2d_bidirectional_memcpy_write_ce_total",
        "activate": True,
        "offset": 3,
        "right_offset": 1,
        # DO NOT CHANGE - there is no title for the test
        "start": "SUM device_to_device_bidirectional_memcpy_write_ce_write2",
        "end": "SUM device_to_device_bidirectional_memcpy_write_ce_total",
        "group_id": 1
    }

    ALL2H_MEMCPY_CE = {
        "name": "all_to_host_memcpy_ce",
        "activate": True,
        "offset": 2,
        "right_offset": 1,
        "start": "Running all_to_host_memcpy_ce",
        "end": "SUM all_to_host_memcpy_ce",
        "group_id": 7
    }

    ALL2H_BIDIRECT_MEMCPY_CE = {
        "name": "all_to_host_bidirectional_memcpy_ce",
        "activate": True,
        "offset": 2,
        "right_offset": 1,
        "start": "Running all_to_host_bidirectional_memcpy_ce",
        "end": "SUM all_to_host_bidirectional_memcpy_ce",
        "group_id": 8
    }

    H2ALL_MAMCPY_CE = {
        "name": "host_to_all_memcpy_ce",
        "activate": True,
        "offset": 2,
        "right_offset": 1,
        "start": "Running host_to_all_memcpy_ce",
        "end": "SUM host_to_all_memcpy_ce",
        "group_id": 9
    }

    H2ALL_BIDIRECT_MAMCPY_CE = {
        "name": "host_to_all_bidirectional_memcpy_ce",
        "activate": True,
        "offset": 2,
        "right_offset": 1,
        "start": "Running host_to_all_bidirectional_memcpy_ce",
        "end": "SUM host_to_all_bidirectional_memcpy_ce",
        "group_id": 10
    }

    ALL2ONE_WRITE_CE = {
        "name": "all_to_one_write_ce",
        "activate": True,
        "offset": 2,
        "right_offset": 1,
        "start": "Running all_to_one_write_ce",
        "end": "SUM all_to_one_write_ce",
        "group_id": 11
    }

    ALL2ONE_READ_CE = {
        "name": "all_to_one_read_ce",
        "activate": True,
        "offset": 2,
        "right_offset": 1,
        "start": "Running all_to_one_read_ce",
        "end": "SUM all_to_one_read_ce",
        "group_id": 12
    }

    ONE2ALL_WRITE_CE = {
        "name": "one_to_all_write_ce",
        "activate": True,
        "offset": 2,
        "right_offset": 1,
        "start": "Running one_to_all_write_ce",
        "end": "SUM one_to_all_write_ce",
        "group_id": 13
    }

    ONE2ALL_READ_CE = {
        "name": "one_to_all_read_ce",
        "activate": True,
        "offset": 2,
        "right_offset": 1,
        "start": "Running one_to_all_read_ce",
        "end": "SUM one_to_all_read_ce",
        "group_id": 14
    }

    # -- memcpy_sm
    H2D_MEMCPY_SM = {
        "name": "host_to_device_memcpy_sm",
        "activate": True,
        "offset": 2,
        "right_offset": 1,
        "start": "Running host_to_device_memcpy_sm",
        "end": "SUM host_to_device_memcpy_sm",
        "group_id": 15
    }

    D2H_MEMCPY_SM = {
        "name": "device_to_host_memcpy_sm",
        "activate": True,
        "offset": 2,
        "right_offset": 1,
        "start": "Running device_to_host_memcpy_sm",
        "end": "SUM device_to_host_memcpy_sm",
        "group_id": 16
    }

    H2DB_MEMCPY_SM = {
        "name": "host_to_device_bidirectional_memcpy_sm",
        "activate": True,
        "offset": 2,
        "right_offset": 1,
        "start": "Running host_to_device_bidirectional_memcpy_sm",
        "end": "SUM host_to_device_bidirectional_memcpy_sm",
        "group_id": 17
    }

    D2HB_MEMCPY_SM = {
        "name": "device_to_host_bidirectional_memcpy_sm",
        "activate": True,
        "offset": 2,
        "right_offset": 1,
        "start": "Running device_to_host_bidirectional_memcpy_sm",
        "end": "SUM device_to_host_bidirectional_memcpy_sm ",
        "group_id": 18
    }

    D2D_READ_MEMCPY_SM = {
        "name": "device_to_device_memcpy_read_sm",
        "activate": True,
        "offset": 2,
        "right_offset": 1,
        "start": "Running device_to_device_memcpy_read_sm",
        "end": "SUM device_to_device_memcpy_read_sm",
        "group_id": 2
    }

    D2D_WRITE_MEMCPY_SM = {
        "name": "device_to_device_memcpy_write_sm",
        "activate": True,
        "offset": 2,
        "right_offset": 1,
        "start": "Running device_to_device_memcpy_write_sm",
        "end": "SUM device_to_device_memcpy_write_sm",
        "group_id": 2
    }

    D2D_READ_BIDIRECT_TOTAL_MEMCPY_SM = {
        "name": "d2d_bidirectional_memcpy_read_sm_total",
        "activate": True,
        "offset": 3,
        "right_offset": 1,
        "start": "SUM device_to_device_bidirectional_memcpy_read_sm_read2",
        "end": "SUM device_to_device_bidirectional_memcpy_read_sm_total",
        "group_id": 2
    }

    D2D_WRITE_BIDIRECT_TOTAL_MEMCPY_SM = {
        "name": "d2d_bidirectional_memcpy_write_sm_total",
        "activate": True,
        "offset": 3,
        "right_offset": 1,
        "start": "SUM device_to_device_bidirectional_memcpy_write_sm_write2",
        "end": "SUM device_to_device_bidirectional_memcpy_write_sm_total",
        "group_id": 2
    }

    ALL2H_MEMCPY_SM = {
        "name": "all_to_host_memcpy_sm",
        "activate": True,
        "offset": 2,
        "right_offset": 1,
        "start": "Running all_to_host_memcpy_sm",
        "end": "SUM all_to_host_memcpy_sm",
        "group_id": 19
    }

    ALL2H_BIDIRECT_MEMCPY_SM = {
        "name": "all_to_host_bidirectional_memcpy_sm",
        "activate": True,
        "offset": 2,
        "right_offset": 1,
        "start": "Running all_to_host_bidirectional_memcpy_sm",
        "end": "SUM all_to_host_bidirectional_memcpy_sm",
        "group_id": 20
    }

    H2ALL_MAMCPY_SM = {
        "name": "host_to_all_memcpy_sm",
        "activate": True,
        "offset": 2,
        "right_offset": 1,
        "start": "Running host_to_all_memcpy_sm",
        "end": "SUM host_to_all_memcpy_sm",
        "group_id": 21
    }

    H2ALL_BIDIRECT_MAMCPY_SM = {
        "name": "host_to_all_bidirectional_memcpy_sm",
        "activate": True,
        "offset": 2,
        "right_offset": 1,
        "start": "Running host_to_all_bidirectional_memcpy_sm",
        "end": "SUM host_to_all_bidirectional_memcpy_sm",
        "group_id": 22
    }

    ALL2ONE_WRITE_SM = {
        "name": "all_to_one_write_sm",
        "activate": True,
        "offset": 2,
        "right_offset": 1,
        "start": "Running all_to_one_write_sm",
        "end": "SUM all_to_one_write_sm",
        "group_id": 23
    }

    ALL2ONE_READ_SM = {
        "name": "all_to_one_read_sm",
        "activate": True,
        "offset": 2,
        "right_offset": 1,
        "start": "Running all_to_one_read_sm",
        "end": "SUM all_to_one_read_sm",
        "group_id": 24
    }

    ONE2ALL_WRITE_SM = {
        "name": "one_to_all_write_sm",
        "activate": True,
        "offset": 2,
        "right_offset": 1,
        "start": "Running one_to_all_write_sm",
        "end": "SUM one_to_all_write_sm",
        "group_id": 25
    }

    ONE2ALL_READ_SM = {
        "name": "one_to_all_read_sm",
        "activate": True,
        "offset": 2,
        "right_offset": 1,
        "start": "Running one_to_all_read_sm",
        "end": "SUM one_to_all_read_sm",
        "group_id": 26
    }

    H_D_LATENCY = {
        "name": "host_device_latency_sm",
        "activate": False,
        "offset": 2,
        "right_offset": 1,
        "start": "Running host_device_latency_sm",
        "end": "SUM host_device_latency_sm",
        "group_id": 27
    }

    D_D_LATENCY = {
        "name": "device_to_device_latency_sm",
        "activate": False,
        "offset": 2,
        "right_offset": 1,
        "start": "Running device_to_device_latency_sm",
        "end": "SUM device_to_device_latency_sm",
        "group_id": 28
    }

    D_LOCAL_COPY = {
        "name": "device_local_copy",
        "activate": False,
        "offset": 2,
        "right_offset": 1,
        "start": "Running device_local_copy",
        "end": "SUM device_local_copy",
        "group_id": 29
    }
