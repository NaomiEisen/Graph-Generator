class NvBandwidthConfig:

    # Group version 1
    GROUPS_INFO = {
    0: {"file_name": "d2h_and_h2d_ce", "test_name": "device <-> host memcpy_ce"},
    1: {"file_name": "d2d_ce", "test_name": "device <-> device memcpy_ce"},
    2: {"file_name": "h2all_and_all2h_ce", "test_name": "all <-> host memcpy_ce"},
    3: {"file_name": "all2one_one2all_ce", "test_name": "all <-> one memcpy_ce"},
    4: {"file_name": "d2h_and_h2d_sm", "test_name": "device <-> host memcpy_sm" },
    5: {"file_name": "d2d_sm", "test_name": "device <-> device memcpy_sm"},
    6: {"file_name": "h2all_and_all2h_sm", "test_name": "all <-> host memcpy_sm"},
    7: {"file_name": "all2one_one2all_sm", "test_name": "all <-> one memcpy_sm"},
    8: {"file_name": "latency_sm", "test_name": "latency_sm - host and device | device to device"},
    9: { "file_name": "device_local_copy", "test_name": "device local copy"},


    # Group version 2
        11: {"file_name": "H2D_memcpy_ce", "test_name": "Host to device memcpy ce"},
        12: {"file_name": "D2H_memcpy_ce", "test_name": "Device to host memcpy_ce"},
        13: {"file_name": "H2DB_memcpy_ce", "test_name": "Host to device bidirectional memcpy_ce"},
        14: {"file_name": "D2HB_memcpy_ce", "test_name": "Device to host bidirectional memcpy_ce"},
        15: {"file_name": "A2H_memcpy_ce", "test_name": "All To Host memcpy_ce"},
        16: {"file_name": "A2HB_memcpy_ce", "test_name": "All To Host Bidirectional memcpy_ce"},
        17: {"file_name": "H2A_memcpy_ce", "test_name": "Host To All memcpy_ce"},
        18: {"file_name": "H2AB_memcpy_ce", "test_name": "Host To All Bidirectional memcpy_ce"},
        19: {"file_name": "D2D_read_write_ce", "test_name": "Device To Device Read&Write memcpy_ce"},
        20: {"file_name": "O2A_write_memcpy_ce", "test_name": "All to One Read memcpy_ce"},
        21: {"file_name": "O2A_read_memcpy_ce", "test_name": "All to One Write memcpy_sm"},
        22: {"file_name": "A2O_write_memcpy_ce", "test_name": "All to One Write memcpy_ce"},
        23: {"file_name": "A2O_read_memcpy_ce", "test_name": "All to One Read memcpy_ce"},

        24: {"file_name": "H2D_memcpy_sm", "test_name": "Host to device memcpy sm"},
        25: {"file_name": "D2H_memcpy_sm", "test_name": "Device to host memcpy_sm"},
        26: {"file_name": "H2DB_memcpy_sm", "test_name": "Host to device bidirectional memcpy_sm"},
        27: {"file_name": "D2HB_memcpy_sm", "test_name": "Device to host bidirectional memcpy_sm"},
        28: {"file_name": "A2H_memcpy_sm", "test_name": "All To Host memcpy_sm"},
        29: {"file_name": "A2HB_memcpy_sm", "test_name": "All To Host Bidirectional memcpy_sm"},
        30: {"file_name": "H2A_memcpy_sm", "test_name": "Host To All memcpy_sm"},
        31: {"file_name": "H2AB_memcpy_sm", "test_name": "Host To All Bidirectional memcpy_sm"},
        32: {"file_name": "D2D_read_write_sm", "test_name": "Device To Device Read&Write memcpy_sm"},
        33: {"file_name": "O2A_write_memcpy_sm", "test_name": "All to One Read memcpy_sm"},
        34: {"file_name": "O2A_read_memcpy_sm", "test_name": "All to One Write memcpy_sm"},
        35: {"file_name": "A2O_write_memcpy_sm", "test_name": "All to One Write memcpy_sm"},
        36: {"file_name": "A2O_read_memcpy_sm", "test_name": "All to One Read memcpy_sm"},
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
        "group_id" : 11 # old 0
    }

    D2H_MEMCPY_CE = {
        "name": "device_to_host_memcpy_ce", 
        "activate": True,
        "offset": 2,
        "right_offset": 1,
        "start": "Running device_to_host_memcpy_ce",  
        "end": "SUM device_to_host_memcpy_ce",
        "group_id" : 12 # old o
    }

    H2DB_MEMCPY_CE = {
        "name": "host_to_device_bidirectional_memcpy_ce", 
        "activate": True,
        "offset": 2,
        "right_offset": 1,
        "start": "Running host_to_device_bidirectional_memcpy_ce",  
        "end": "SUM host_to_device_bidirectional_memcpy_ce",
        "group_id" : 13 # old 0
    }

    D2HB_MEMCPY_CE = {
        "name": "device_to_host_bidirectional_memcpy_ce", 
        "activate": True,
        "offset": 2,
        "right_offset": 1,
        "start": "Running device_to_host_bidirectional_memcpy_ce",  
        "end": "SUM device_to_host_bidirectional_memcpy_ce ",
        "group_id" : 14 # old 0
    }

    D2D_READ_MEMCPY_CE = {
        "name": "d2d_memcpy_read_ce",
        "activate": True,
        "offset": 2,
        "right_offset": 1,
        "start": "Running device_to_device_memcpy_read_ce",
        "end": "SUM device_to_device_memcpy_read_ce",
        "group_id": 19
    }

    D2D_WRITE_MEMCPY_CE = {
        "name": "d2d_memcpy_write_ce",
        "activate": True,
        "offset": 2,
        "right_offset": 1,
        "start": "Running device_to_device_memcpy_write_ce",
        "end": "SUM device_to_device_memcpy_write_ce",
        "group_id": 19
    }

    D2D_READ_BIDIRECT_TOTAL_MEMCPY_CE = {
        "name": "d2d_bidirectional_memcpy_read_ce_total",
        "activate": True,
        "offset": 3,
        "right_offset": 1,
        # DO NOT CHANGE - there are no title for the test
        "start": "SUM device_to_device_bidirectional_memcpy_read_ce_read2",
        "end": "SUM device_to_device_bidirectional_memcpy_read_ce_total",
        "group_id": 19
    }

    D2D_WRITE_BIDIRECT_TOTAL_MEMCPY_CE = {
        "name": "d2d_bidirectional_memcpy_write_ce_total",
        "activate": True,
        "offset": 3,
        "right_offset": 1,
        # DO NOT CHANGE - there are no title for the test
        "start": "SUM device_to_device_bidirectional_memcpy_write_ce_write2",
        "end": "SUM device_to_device_bidirectional_memcpy_write_ce_total",
        "group_id": 19
    }

    ALL2H_MEMCPY_CE = {
        "name": "all_to_host_memcpy_ce",
        "activate": True,
        "offset": 2,
        "right_offset": 1,
        "start": "Running all_to_host_memcpy_ce",
        "end": "SUM all_to_host_memcpy_ce",
        "group_id": 15
    }

    ALL2H_BIDIRECT_MEMCPY_CE = {
        "name": "all_to_host_bidirectional_memcpy_ce",
        "activate": True,
        "offset": 2,
        "right_offset": 1,
        "start": "Running all_to_host_bidirectional_memcpy_ce",
        "end": "SUM all_to_host_bidirectional_memcpy_ce",
        "group_id": 16
    }

    H2ALL_MAMCPY_CE = {
        "name": "host_to_all_memcpy_ce",
        "activate": True,
        "offset": 2,
        "right_offset": 1,
        "start": "Running host_to_all_memcpy_ce",
        "end": "SUM host_to_all_memcpy_ce",
        "group_id": 17
    }

    H2ALL_BIDIRECT_MAMCPY_CE = {
        "name": "host_to_all_bidirectional_memcpy_ce",
        "activate": True,
        "offset": 2,
        "right_offset": 1,
        "start": "Running host_to_all_bidirectional_memcpy_ce",
        "end": "SUM host_to_all_bidirectional_memcpy_ce",
        "group_id": 18
    }

    ALL2ONE_WRITE_CE = {
        "name": "all_to_one_write_ce",
        "activate": True,
        "offset": 2,
        "right_offset": 1,
        "start": "Running all_to_one_write_ce",
        "end": "SUM all_to_one_write_ce",
        "group_id": 22
    }

    ALL2ONE_READ_CE = {
        "name": "all_to_one_read_ce",
        "activate": True,
        "offset": 2,
        "right_offset": 1,
        "start": "Running all_to_one_read_ce",
        "end": "SUM all_to_one_read_ce",
        "group_id": 23
    }

    ONE2ALL_WRITE_CE = {
        "name": "one_to_all_write_ce",
        "activate": True,
        "offset": 2,
        "right_offset": 1,
        "start": "Running one_to_all_write_ce",
        "end": "SUM one_to_all_write_ce",
        "group_id": 20
    }

    ONE2ALL_READ_CE = {
        "name": "one_to_all_read_ce",
        "activate": True,
        "offset": 2,
        "right_offset": 1,
        "start": "Running one_to_all_read_ce",
        "end": "SUM one_to_all_read_ce",
        "group_id": 21
    }

    # -- memcpy_sm
    H2D_MEMCPY_SM = {
        "name": "host_to_device_memcpy_sm",
        "activate": True,
        "offset": 2,
        "right_offset": 1,
        "start": "Running host_to_device_memcpy_sm",
        "end": "SUM host_to_device_memcpy_sm",
        "group_id": 24
    }

    D2H_MEMCPY_SM = {
        "name": "device_to_host_memcpy_sm",
        "activate": True,
        "offset": 2,
        "right_offset": 1,
        "start": "Running device_to_host_memcpy_sm",
        "end": "SUM device_to_host_memcpy_sm",
        "group_id": 25
    }

    H2DB_MEMCPY_SM = {
        "name": "host_to_device_bidirectional_memcpy_sm",
        "activate": True,
        "offset": 2,
        "right_offset": 1,
        "start": "Running host_to_device_bidirectional_memcpy_sm",
        "end": "SUM host_to_device_bidirectional_memcpy_sm",
        "group_id": 26
    }

    D2HB_MEMCPY_SM = {
        "name": "device_to_host_bidirectional_memcpy_sm",
        "activate": True,
        "offset": 2,
        "right_offset": 1,
        "start": "Running device_to_host_bidirectional_memcpy_sm",
        "end": "SUM device_to_host_bidirectional_memcpy_sm ",
        "group_id": 27
    }

    D2D_READ_MEMCPY_SM = {
        "name": "device_to_device_memcpy_read_sm",
        "activate": True,
        "offset": 2,
        "right_offset": 1,
        "start": "Running device_to_device_memcpy_read_sm",
        "end": "SUM device_to_device_memcpy_read_sm",
        "group_id": 32
    }

    D2D_WRITE_MEMCPY_SM = {
        "name": "device_to_device_memcpy_write_sm",
        "activate": True,
        "offset": 2,
        "right_offset": 1,
        "start": "Running device_to_device_memcpy_write_sm",
        "end": "SUM device_to_device_memcpy_write_sm",
        "group_id": 32
    }

    D2D_READ_BIDIRECT_TOTAL_MEMCPY_SM = {
        "name": "d2d_bidirectional_memcpy_read_sm_total",
        "activate": True,
        "offset": 3,
        "right_offset": 1,
        "start": "SUM device_to_device_bidirectional_memcpy_read_sm_read2",
        "end": "SUM device_to_device_bidirectional_memcpy_read_sm_total",
        "group_id": 32
    }

    D2D_WRITE_BIDIRECT_TOTAL_MEMCPY_SM = {
        "name": "d2d_bidirectional_memcpy_write_sm_total",
        "activate": True,
        "offset": 3,
        "right_offset": 1,
        "start": "SUM device_to_device_bidirectional_memcpy_write_sm_write2",
        "end": "SUM device_to_device_bidirectional_memcpy_write_sm_total",
        "group_id": 32
    }

    ALL2H_MEMCPY_SM = {
        "name": "all_to_host_memcpy_sm",
        "activate": True,
        "offset": 2,
        "right_offset": 1,
        "start": "Running all_to_host_memcpy_sm",
        "end": "SUM all_to_host_memcpy_sm",
        "group_id": 28
    }

    ALL2H_BIDIRECT_MEMCPY_SM = {
        "name": "all_to_host_bidirectional_memcpy_sm",
        "activate": True,
        "offset": 2,
        "right_offset": 1,
        "start": "Running all_to_host_bidirectional_memcpy_sm",
        "end": "SUM all_to_host_bidirectional_memcpy_sm",
        "group_id": 29
    }

    H2ALL_MAMCPY_SM = {
        "name": "host_to_all_memcpy_sm",
        "activate": True,
        "offset": 2,
        "right_offset": 1,
        "start": "Running host_to_all_memcpy_sm",
        "end": "SUM host_to_all_memcpy_sm",
        "group_id": 30
    }

    H2ALL_BIDIRECT_MAMCPY_SM = {
        "name": "host_to_all_bidirectional_memcpy_sm",
        "activate": True,
        "offset": 2,
        "right_offset": 1,
        "start": "Running host_to_all_bidirectional_memcpy_sm",
        "end": "SUM host_to_all_bidirectional_memcpy_sm",
        "group_id": 31
    }

    ALL2ONE_WRITE_SM = {
        "name": "all_to_one_write_sm",
        "activate": True,
        "offset": 2,
        "right_offset": 1,
        "start": "Running all_to_one_write_sm",
        "end": "SUM all_to_one_write_sm",
        "group_id": 35
    }

    ALL2ONE_READ_SM = {
        "name": "all_to_one_read_sm",
        "activate": True,
        "offset": 2,
        "right_offset": 1,
        "start": "Running all_to_one_read_sm",
        "end": "SUM all_to_one_read_sm",
        "group_id": 36
    }

    ONE2ALL_WRITE_SM = {
        "name": "one_to_all_write_sm",
        "activate": True,
        "offset": 2,
        "right_offset": 1,
        "start": "Running one_to_all_write_sm",
        "end": "SUM one_to_all_write_sm",
        "group_id": 33
    }

    ONE2ALL_READ_SM = {
        "name": "one_to_all_read_sm",
        "activate": True,
        "offset": 2,
        "right_offset": 1,
        "start": "Running one_to_all_read_sm",
        "end": "SUM one_to_all_read_sm",
        "group_id": 34
    }

    H_D_LATENCY = {
        "name": "host_device_latency_sm",
        "activate": False,
        "offset": 2,
        "right_offset": 1,
        "start": "Running host_device_latency_sm",
        "end": "SUM host_device_latency_sm",
        "group_id": 8
    }

    D_D_LATENCY = {
        "name": "device_to_device_latency_sm",
        "activate": False,
        "offset": 2,
        "right_offset": 1,
        "start": "Running device_to_device_latency_sm",
        "end": "SUM device_to_device_latency_sm",
        "group_id": 8
    }

    D_LOCAL_COPY = {
        "name": "device_local_copy",
        "activate": False,
        "offset": 2,
        "right_offset": 1,
        "start": "Running device_local_copy",
        "end": "SUM device_local_copy",
        "group_id": 9
    }

    #
    # D2D_READ_MEMCPY_CE = {
    #     "name": "d2d_memcpy_read_ce",
    #     "activate": False,
    #     "offset": 2,
    #     "right_offset": 1,
    #     "start": "Running device_to_device_memcpy_read_ce",
    #     "end": "SUM device_to_device_memcpy_read_ce",
    #     "group_id" : 1
    # }
    #
    # D2D_WRITE_MEMCPY_CE = {
    #     "name": "d2d_memcpy_write_ce",
    #     "activate": False,
    #     "offset": 2,
    #     "right_offset": 1,
    #     "start": "Running device_to_device_memcpy_write_ce",
    #     "end": "SUM device_to_device_memcpy_write_ce",
    #     "group_id" : 1
    # }
    #
    # D2D_READ_BIDIRECT_TOTAL_MEMCPY_CE = {
    #     "name": "d2d_bidirectional_memcpy_read_ce_total",
    #     "activate": False,
    #     "offset": 3,
    #     "right_offset": 1,
    #     # DO NOT CHANGE - there are no title for the test
    #     "start": "SUM device_to_device_bidirectional_memcpy_read_ce_read2",
    #     "end": "SUM device_to_device_bidirectional_memcpy_read_ce_total",
    #     "group_id" : 1
    # }
    #
    # D2D_WRITE_BIDIRECT_TOTAL_MEMCPY_CE = {
    #     "name": "d2d_bidirectional_memcpy_write_ce_total",
    #     "activate": False,
    #     "offset": 3,
    #     "right_offset": 1,
    #     # DO NOT CHANGE - there are no title for the test
    #     "start": "SUM device_to_device_bidirectional_memcpy_write_ce_write2",
    #     "end": "SUM device_to_device_bidirectional_memcpy_write_ce_total",
    #     "group_id" : 1
    # }
    #
    # ALL2H_MEMCPY_CE = {
    #     "name": "all_to_host_memcpy_ce",
    #     "activate": False,
    #     "offset": 2,
    #     "right_offset": 1,
    #     "start": "Running all_to_host_memcpy_ce",
    #     "end": "SUM all_to_host_memcpy_ce",
    #     "group_id" : 2
    # }
    #
    # ALL2H_BIDIRECT_MEMCPY_CE = {
    #     "name": "all_to_host_bidirectional_memcpy_ce",
    #     "activate": False,
    #     "offset": 2,
    #     "right_offset": 1,
    #     "start": "Running all_to_host_bidirectional_memcpy_ce",
    #     "end": "SUM all_to_host_bidirectional_memcpy_ce",
    #     "group_id" : 2
    # }
    #
    # H2ALL_MAMCPY_CE = {
    #     "name": "host_to_all_memcpy_ce",
    #     "activate": False,
    #     "offset": 2,
    #     "right_offset": 1,
    #     "start": "Running host_to_all_memcpy_ce",
    #     "end": "SUM host_to_all_memcpy_ce",
    #     "group_id" : 2
    # }
    #
    # H2ALL_BIDIRECT_MAMCPY_CE = {
    #     "name": "host_to_all_bidirectional_memcpy_ce",
    #     "activate": False,
    #     "offset": 2,
    #     "right_offset": 1,
    #     "start": "Running host_to_all_bidirectional_memcpy_ce",
    #     "end": "SUM host_to_all_bidirectional_memcpy_ce" ,
    #     "group_id" : 2
    # }
    #
    # ALL2ONE_WRITE_CE = {
    #     "name": "all_to_one_write_ce",
    #     "activate": False,
    #     "offset": 2,
    #     "right_offset": 1,
    #     "start": "Running all_to_one_write_ce",
    #     "end": "SUM all_to_one_write_ce" ,
    #     "group_id" : 3
    # }
    #
    # ALL2ONE_READ_CE = {
    #     "name": "all_to_one_read_ce",
    #     "activate": False,
    #     "offset": 2,
    #     "right_offset": 1,
    #     "start": "Running all_to_one_read_ce",
    #     "end": "SUM all_to_one_read_ce",
    #     "group_id" : 3
    # }
    #
    # ONE2ALL_WRITE_CE = {
    #     "name": "one_to_all_write_ce",
    #     "activate": False,
    #     "offset": 2,
    #     "right_offset": 1,
    #     "start": "Running one_to_all_write_ce",
    #     "end": "SUM one_to_all_write_ce" ,
    #     "group_id" : 3
    # }
    #
    # ONE2ALL_READ_CE = {
    #     "name": "one_to_all_read_ce",
    #     "activate": False,
    #     "offset": 2,
    #     "right_offset": 1,
    #     "start": "Running one_to_all_read_ce",
    #     "end": "SUM one_to_all_read_ce"  ,
    #     "group_id" : 3
    # }
    #
    # # -- memcpy_sm
    # H2D_MEMCPY_SM = {
    #     "name": "host_to_device_memcpy_sm",
    #     "activate": False,
    #     "offset": 2,
    #     "right_offset": 1,
    #     "start": "Running host_to_device_memcpy_sm",
    #     "end": "SUM host_to_device_memcpy_sm",
    #     "group_id" : 4
    # }
    #
    # D2H_MEMCPY_SM = {
    #     "name": "device_to_host_memcpy_sm",
    #     "activate": False,
    #     "offset": 2,
    #     "right_offset": 1,
    #     "start": "Running device_to_host_memcpy_sm",
    #     "end": "SUM device_to_host_memcpy_sm"  ,
    #     "group_id" : 4
    # }
    #
    # H2DB_MEMCPY_SM = {
    #     "name": "host_to_device_bidirectional_memcpy_sm",
    #     "activate": False,
    #     "offset": 2,
    #     "right_offset": 1,
    #     "start": "Running host_to_device_bidirectional_memcpy_sm",
    #     "end": "SUM host_to_device_bidirectional_memcpy_sm",
    #     "group_id" : 4
    # }
    #
    # D2HB_MEMCPY_SM = {
    #     "name": "device_to_host_bidirectional_memcpy_sm",
    #     "activate": False,
    #     "offset": 2,
    #     "right_offset": 1,
    #     "start": "Running device_to_host_bidirectional_memcpy_sm",
    #     "end": "SUM device_to_host_bidirectional_memcpy_sm "   ,
    #     "group_id" : 4
    # }
    #
    # D2D_READ_MEMCPY_SM = {
    #     "name": "device_to_device_memcpy_read_sm",
    #     "activate": False,
    #     "offset": 2,
    #     "right_offset": 1,
    #     "start": "Running device_to_device_memcpy_read_sm",
    #     "end": "SUM device_to_device_memcpy_read_sm",
    #     "group_id" : 5
    # }
    #
    # D2D_WRITE_MEMCPY_SM = {
    #     "name": "device_to_device_memcpy_write_sm",
    #     "activate": False,
    #     "offset": 2,
    #     "right_offset": 1,
    #     "start": "Running device_to_device_memcpy_write_sm",
    #     "end": "SUM device_to_device_memcpy_write_sm",
    #     "group_id" : 5
    # }
    #
    # D2D_READ_BIDIRECT_TOTAL_MEMCPY_SM = {
    #     "name": "d2d_bidirectional_memcpy_read_sm_total",
    #     "activate": False,
    #     "offset": 3,
    #     "right_offset": 1,
    #     "start": "SUM device_to_device_bidirectional_memcpy_read_sm_read2",
    #     "end": "SUM device_to_device_bidirectional_memcpy_read_sm_total",
    #     "group_id" : 5
    # }
    #
    # D2D_WRITE_BIDIRECT_TOTAL_MEMCPY_SM = {
    #     "name": "d2d_bidirectional_memcpy_write_sm_total",
    #     "activate": False,
    #     "offset": 3,
    #     "right_offset": 1,
    #     "start": "SUM device_to_device_bidirectional_memcpy_write_sm_write2",
    #     "end": "SUM device_to_device_bidirectional_memcpy_write_sm_total",
    #     "group_id" : 5
    # }
    #
    # ALL2H_MEMCPY_SM = {
    #     "name": "all_to_host_memcpy_sm",
    #     "activate": False,
    #     "offset": 2,
    #     "right_offset": 1,
    #     "start": "Running all_to_host_memcpy_sm",
    #     "end": "SUM all_to_host_memcpy_sm"  ,
    #     "group_id" : 6
    # }
    #
    # ALL2H_BIDIRECT_MEMCPY_SM = {
    #     "name": "all_to_host_bidirectional_memcpy_sm",
    #     "activate": False,
    #     "offset": 2,
    #     "right_offset": 1,
    #     "start": "Running all_to_host_bidirectional_memcpy_sm",
    #     "end": "SUM all_to_host_bidirectional_memcpy_sm" ,
    #     "group_id" : 6
    # }
    #
    # H2ALL_MAMCPY_SM = {
    #     "name": "host_to_all_memcpy_sm",
    #     "activate": False,
    #     "offset": 2,
    #     "right_offset": 1,
    #     "start": "Running host_to_all_memcpy_sm",
    #     "end": "SUM host_to_all_memcpy_sm" ,
    #     "group_id" : 6
    # }
    #
    # H2ALL_BIDIRECT_MAMCPY_SM = {
    #     "name": "host_to_all_bidirectional_memcpy_sm",
    #     "activate": False,
    #     "offset": 2,
    #     "right_offset": 1,
    #     "start": "Running host_to_all_bidirectional_memcpy_sm",
    #     "end": "SUM host_to_all_bidirectional_memcpy_sm" ,
    #     "group_id" : 6
    # }
    #
    # ALL2ONE_WRITE_SM = {
    #     "name": "all_to_one_write_sm",
    #     "activate": False,
    #     "offset": 2,
    #     "right_offset": 1,
    #     "start": "Running all_to_one_write_sm",
    #     "end": "SUM all_to_one_write_sm"  ,
    #     "group_id" : 7
    # }
    #
    # ALL2ONE_READ_SM = {
    #     "name": "all_to_one_read_sm",
    #     "activate": False,
    #     "offset": 2,
    #     "right_offset": 1,
    #     "start": "Running all_to_one_read_sm",
    #     "end": "SUM all_to_one_read_sm",
    #     "group_id" : 7
    # }
    #
    # ONE2ALL_WRITE_SM = {
    #     "name": "one_to_all_write_sm",
    #     "activate": False,
    #     "offset": 2,
    #     "right_offset": 1,
    #     "start": "Running one_to_all_write_sm",
    #     "end": "SUM one_to_all_write_sm" ,
    #     "group_id" : 7
    # }
    #
    # ONE2ALL_READ_SM = {
    #     "name": "one_to_all_read_sm",
    #     "activate": False,
    #     "offset": 2,
    #     "right_offset": 1,
    #     "start": "Running one_to_all_read_sm",
    #     "end": "SUM one_to_all_read_sm" ,
    #     "group_id" : 7
    # }
    #
    # H_D_LATENCY = {
    #     "name": "host_device_latency_sm",
    #     "activate": False,
    #     "offset": 2,
    #     "right_offset": 1,
    #     "start": "Running host_device_latency_sm",
    #     "end": "SUM host_device_latency_sm" ,
    #     "group_id" : 8
    # }
    #
    # D_D_LATENCY = {
    #     "name": "device_to_device_latency_sm",
    #     "activate": False,
    #     "offset": 2,
    #     "right_offset": 1,
    #     "start": "Running device_to_device_latency_sm",
    #     "end": "SUM device_to_device_latency_sm" ,
    #     "group_id" : 8
    # }
    #
    # D_LOCAL_COPY = {
    #     "name": "device_local_copy",
    #     "activate": False,
    #     "offset": 2,
    #     "right_offset": 1,
    #     "start": "Running device_local_copy",
    #     "end": "SUM device_local_copy" ,
    #     "group_id" : 9
    # }
    #
