import os
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator

from utils.colors import ColorPalette
from utils.handle_data import load_data_matrix_format

def plot_graph(data, graph_config, file_name, test_name):
    """
    Plots the data from the DataFrame with dots and connecting lines.
    """
    plt.figure(figsize=(graph_config.WIDTH, graph_config.HEIGHT))

    # Use the first column as X-axis
    x_axis = data.iloc[:, 0]

    # Loop through the rest of the columns as Y-axes
    for i in range(1, data.shape[1]):
        y_axis = data.iloc[:, i]
        y_label = data.columns[i]  # Default y-label from column name
        color = graph_config.COLOR_THEME[i % len(graph_config.COLOR_THEME)]  # Cycle through colors
        plt.plot(x_axis, y_axis, marker='o', linestyle='-', label=y_label, color=color)

    # Turn off scientific notation and use plain numbers
    #plt.ticklabel_format(style='plain', axis='both')

    # Increase resolution by adding more y-axis ticks
    plt.gca().yaxis.set_major_locator(MaxNLocator(integer=True, nbins=graph_config.Y_NBINS))

    # Set title with optional LABEL prefix
    plt.title(graph_config.TITLE if graph_config.TITLE else f"{file_name}".strip())

    # Labels
    plt.xlabel(graph_config.X_AXIS if graph_config.X_AXIS else data.columns[0])
    plt.ylabel(graph_config.Y_AXIS)  # Use custom y-label if set
    plt.legend()
    plt.grid()

    # Save the graph
    #save_graphs(plt, file_name_without_extension)

    # Show the plot
    plt.show()