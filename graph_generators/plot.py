import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from matplotlib.ticker import MaxNLocator

from utils.general import  save_graphs

#TODO: make it more generic!!

def plot_single_lines_graph(data, graph_config, file_name, test_name):
    """
    Plots the data from the DataFrame with dots and connecting lines.
    """

    fig, ax = plt.subplots()

    # Define X range (min=0, max from first column)
    x_min, x_max = 0, pd.to_numeric(data.iloc[:, 0]).max()
    x_range = np.linspace(x_min, x_max, num=len(data))  # Generate evenly spaced values

    # Loop through Y columns (other than the first one)
    for i in range(1, data.shape[1]):
        y_axis = pd.to_numeric(data.iloc[:, i], errors='coerce')  # Convert to numbers
        y_label = data.columns[i]  # Use column header as label
        color = graph_config.COLOR_THEME[i % len(graph_config.COLOR_THEME)]  # Assign color
        ax.plot(x_range, y_axis, marker='o', linestyle='-', label=y_label, color=color)


    # Set x-axis limits
    ax.set_xlim(x_min, x_max)
    ax.ticklabel_format(style='plain', axis='x')

    # Increase resolution by adding more y-axis ticks
    ax.yaxis.set_major_locator(MaxNLocator(integer=True, nbins=graph_config.Y_NBINS))

    # Titles and labels
    ax.set_title(test_name)
    ax.set_xlabel(graph_config.X_AXIS if graph_config.X_AXIS else data.columns[0])
    ax.set_ylabel(graph_config.Y_AXIS)
    ax.legend()
    ax.grid()

    # Save the graph
    save_graphs(plt, file_name)

# TODO: find the shared columns automatically
def plot_subplots_line_graph(data, graph_config, file_name, number_plots=2):
    fig, ax = plt.subplots(nrows=number_plots, constrained_layout=True)

    # Define X range (min=0, max from first column)
    x_min, x_max = 0, pd.to_numeric(data.iloc[:, 0]).max()
    x_range = np.linspace(x_min, x_max, num=len(data))  # Generate evenly spaced values

    color_counter = 1
    for p in range(number_plots):
    # Loop through Y columns (other than the first one)
        for i in range(1, data.shape[1]//number_plots + 1):
            y_axis = pd.to_numeric(data.iloc[:, color_counter], errors='coerce')  # Convert to numbers
            y_label = data.columns[i]  # Use column header as label
            color = graph_config.COLOR_THEME[color_counter % len(graph_config.COLOR_THEME)]  # Assign color
            ax[p].plot(x_range, y_axis, marker='o', linestyle='-', label=y_label, color=color)
            color_counter += 1

        # Set x-axis limits
        ax[p].set_xlim(x_min, x_max)

        # Titles and labels
        ax[p].set_title(graph_config.SUB_PLOT_TITLE[p])
        ax[p].set_xlabel(graph_config.X_AXIS if graph_config.X_AXIS else data.columns[0])
        ax[p].set_ylabel(graph_config.Y_AXIS[p])
        ax[p].legend()
        ax[p].grid()

    fig.suptitle(graph_config.TITLE, fontsize=graph_config.TITLE_SIZE)
    # Save the graph
    save_graphs(plt, file_name)

