class AllReduceConfig:
    FILE_NAME = "all_reduce"

    COLUMNS_TO_COMPARE = [
        "size(MB)",
        "tavg(usec)",
        "avgbw(GB/sec)"]

    # Tests configs
    ALL_REDUCE = {
        "name": "All Reduce",
        "activate": True,
        "offset": 1,
        "right_offset": 0,
        "start": "NCCL version",
        "end": "",
    }