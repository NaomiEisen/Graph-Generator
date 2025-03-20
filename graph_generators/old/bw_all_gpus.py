import os
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator

from utils.colors import ColorPalette
from utils.handle_data import load_data_matrix_format
#
#
# class BwAll:
#     # y axes nbins
#     Y_NBINS = 20
#
#     # axis labels
#     X_LABEL = 'Transfer Size (Bytes)'
#     Y_LABEL = 'Bandwidth(GB/s)'
#
#     # title
#     TITLE  = 'Transfer size to Bandwidth using all gpus'
#
# def bandwidth_all_gpu_test(files):
#     """
#     Plots the data from the DataFrame with dots and connecting lines.
#     """
#     plt.figure(figsize=(Const.WIDTH, Const.HEIGHT))
#     data = load_data_matrix_format(files[0])
#     print(data)
#
#     # Plot the data
#     plt.plot(data.iloc[:, 0], data.iloc[:, 1], marker='o', linestyle='-', label='Bandwidth(GB/s)', color= ColorPalette.PEACH)
#
#     # Turn off scientific notation and use regular number formatting
#     plt.ticklabel_format(style='plain', axis='both')
#
#     # Increase resolution by adding more ticks on y-axis (adjust 'nbins' as needed)
#     plt.gca().yaxis.set_major_locator(MaxNLocator(integer=True, nbins=BwAll.Y_NBINS))  # Change nbins to control the number of ticks
#
#     # Extract filename without extension
#     file_name_without_extension = os.path.splitext(os.path.basename(files[0]))[0]
#
#     # Add the title with the file name
#     plt.title(f"{BwAll.TITLE} - {file_name_without_extension}")
#
#     # Labels and title
#     plt.xlabel(BwAll.X_LABEL)
#     plt.ylabel(BwAll.Y_LABEL)
#     plt.legend()
#     plt.grid()
#
#     # Show the plot
#     plt.show()
