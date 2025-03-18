import os
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.ticker import MaxNLocator

from colors import ColorPalette, Const
from utils.handle_data import get_files_list, load_data_matrix_format, save_graphs

class BwAvg:
    # Define constants for plot customization
    Y_NBINS = 20

    # Axis labels
    X_LABEL = ''
    Y_LABEL = ''

    # Plot title - the default is the file name (if you prefer this do not change)
    TITLE = 'Average Transfer Size to Bandwidth (All GPUs)'
    OUTPUT_FILE_NAME = 'graph'

    # Plot colors (example: use ColorPalette from existing colors)
    COLORS = ColorPalette.BASIC_THEME

def bandwidth_avg_gpu(args):
    """
    Plots the average data from multiple files as a single graph.
    Computes the average value for each X (first column) across all files for each Y-column.
    """
    
    # If input is a directory, get all files inside
    files = get_files_list(args)

    # Initialize a list to store dataframes and a variable for X values
    all_data = []
    x_values = None
    y_labels = []

    # Load the data from each file
    for file in files:
        data = load_data_matrix_format(file)

        # Extract the X values (first column)
        if x_values is None:
            x_values = data.iloc[:, 0]
            # Collect the Y-labels from the columns (excluding the first one)
            y_labels = data.columns[1:]

        
        # Append the data (excluding the first column) to the list
        all_data.append(data.iloc[:, 1:])

    # Stack all dataframes vertically (to stack all Y values from each file)
    combined_data = pd.concat(all_data, axis=0, ignore_index=True)

    # Compute the average for each Y-column (i.e., each column from the second onwards)
    # Now averaging over rows (axis=0) for each X value
    avg_data = combined_data.groupby(combined_data.index % len(x_values)).mean()

    # Plotting the average data for each Y-column
    plt.figure(figsize=(Const.WIDTH, Const.HEIGHT)) 

    # Loop over the Y columns and plot each one separately
    for i, column in enumerate(avg_data.columns):
        plt.plot(x_values, avg_data[column], marker='o', linestyle='-', label=f"Average {y_labels[i]}", color=BwAvg.COLORS[i % len(BwAvg.COLORS)])

    # Turn off scientific notation and use plain numbers
    plt.ticklabel_format(style='plain', axis='both')

    # Increase resolution by adding more y-axis ticks
    plt.gca().yaxis.set_major_locator(MaxNLocator(integer=True, nbins=BwAvg.Y_NBINS))

    # Set title
    plt.title(BwAvg.TITLE)

    # Set labels
    plt.xlabel(BwAvg.X_LABEL if BwAvg.X_LABEL else 'X-axis')
    plt.ylabel(BwAvg.Y_LABEL if BwAvg.Y_LABEL else '')
    plt.legend()
    plt.grid()

    # Save the graph
    save_graphs(plt, BwAvg.OUTPUT_FILE_NAME)
