import matplotlib.pyplot as plt

from globals import ColorPalette, Const
from helpers.handle_data import load_data_matrix_format

class NcclTest:
    # test columns
    SIZE_MB = 'size(MB)'
    TAVG_USEC = 'tavg(usec)'
    TMIN_USEC = 'tmin(usec)'
    TMAX_USEC = 'tmax(usec)'
    AVGBW_GB_SEC = 'avgbw(GB/sec)'
    MAXBW_GB_SEC = 'maxbw(GB/sec)'
    MINBW_GB_SEC = 'minbw(GB/sec)'

    # axis labels
    X_LABEL = 'Size (MB)'
    Y_LABEL_TIME = 'Time (usec)'
    Y_LABEL_BANDWIDTH = 'Bandwidth (GB/sec)'

    # title
    TIME_TITLE = 'Performance Graph'
    BANDWITH_TITLE = 'Bandwidth Performance Graph'

    # List of colors for multiple lines
    COLORS = ColorPalette.SUNSET_THEME

    
def nccl_test_graph(files):
    """
    Plots the data from the DataFrame with dots and connecting lines.
    """
    plt.figure(figsize=(Const.WIDTH, Const.HEIGHT))

    # Skip the first row
    data = load_data_matrix_format(files[0])
    
    # usec representation
    plt.plot(data[NcclTest.SIZE_MB], data[NcclTest.TAVG_USEC], marker='o', linestyle='-', label='Avg Time (usec)', color= NcclTest.COLORS[0])
    plt.plot(data[NcclTest.SIZE_MB], data[NcclTest.TMIN_USEC], marker='o', linestyle='-', label='Min Time (usec)', color= NcclTest.COLORS[1])
    plt.plot(data[NcclTest.SIZE_MB], data[NcclTest.TMAX_USEC], marker='o', linestyle='-', label='Max Time (usec)', color=NcclTest.COLORS[2])

    plt.xlabel(NcclTest.X_LABEL)
    plt.ylabel(NcclTest.Y_LABEL_TIME)
    plt.title(NcclTest.TIME_TITLE)
    plt.legend()
    plt.grid()
    plt.show()

    # usec representation
    plt.plot(data[NcclTest.SIZE_MB], data[NcclTest.AVGBW_GB_SEC], marker='o', linestyle='-', label='Avg Bandwidth (GB/sec)', color= NcclTest.COLORS[0])
    plt.plot(data[NcclTest.SIZE_MB], data[NcclTest.MAXBW_GB_SEC], marker='o', linestyle='-', label='Max Bandwidth (GB/sec)', color= NcclTest.COLORS[1])
    plt.plot(data[NcclTest.SIZE_MB], data[NcclTest.MINBW_GB_SEC], marker='o', linestyle='-', label='Min Bandwidth (GB/sec)', color= NcclTest.COLORS[2])

    plt.xlabel(NcclTest.X_LABEL)
    plt.ylabel(NcclTest.Y_LABEL_BANDWIDTH)
    plt.title(NcclTest.BANDWITH_TITLE)
    plt.legend()
    plt.grid()
    plt.show()