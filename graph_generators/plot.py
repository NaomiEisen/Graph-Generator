import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from matplotlib.ticker import MaxNLocator

from utils.handle_data import  save_graphs


def plot_lines_graph(data, graph_config, file_name, test_name):
    """
    Plots the data from the DataFrame with dots and connecting lines.
    """

    plt.rcParams.update({
        'axes.facecolor': '#1e1e1e',  # Dark gray background for the plot area
        'axes.edgecolor': 'white',  # White borders for the axes
        'axes.labelcolor': 'white',  # White color for axis labels
        'axes.labelsize': graph_config.AXIS_LABEL_FONT_SIZE,  # Font size for x and y axis labels
        'xtick.color': 'white',  # White ticks along the x-axis
        'ytick.color': 'white',  # White ticks along the y-axis
        'xtick.labelsize': 18,  # Font size for x-axis tick labels
        'ytick.labelsize': 18,  # Font size for y-axis tick labels
        'grid.color': '#444444',  # Gridline color
        'grid.alpha': 0.5,  # Make the gridlines slightly transparent
        'text.color': 'white',  # White text for titles and annotations
        'figure.facecolor': '#1e1e1e',  # Dark background for the figure
        'figure.figsize': (graph_config.WIDTH, graph_config.HEIGHT),  #  figure size (in inches)
        'lines.linewidth': 2,  # Thicker lines for better visibility
        'lines.color': 'white',  # Default line color (can be overridden)
        'legend.fontsize': graph_config.LEGEND_FONT_SIZE,
        'axes.titleweight': 'bold',  # Make titles bold
        'axes.titlesize': graph_config.TITLE_SIZE  # Title font size
    })


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