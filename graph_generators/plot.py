import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from matplotlib.ticker import MaxNLocator

from utils.handle_data import load_data_matrix_format, save_graphs


def plot_lines_graph(data, graph_config, file_name, test_name):
    """
    Plots the data from the DataFrame with dots and connecting lines.
    """
    fig, ax = plt.subplots(figsize=(graph_config.WIDTH, graph_config.HEIGHT))

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
    ax.set_title(test_name, fontsize=graph_config.TITLE_SIZE)
    ax.set_xlabel(graph_config.X_AXIS if graph_config.X_AXIS else data.columns[0], fontsize=graph_config.AXIS_LABEL_FONT_SIZE)
    ax.set_ylabel(graph_config.Y_AXIS, fontsize=graph_config.AXIS_LABEL_FONT_SIZE)
    ax.legend()
    ax.grid()

    # Save the graph
    save_graphs(plt, file_name)