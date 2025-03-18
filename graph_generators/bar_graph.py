from matplotlib import pyplot as plt
import numpy as np
import pandas as pd

from utils.handle_data import save_graphs


def plot_bar_graph(data, graph_config, file_name):
    """
    Plots a bar graph for the combined data with sections representing rows.
    Each section will have multiple bars, one for each column.
    
    :param data: The Pandas DataFrame containing the data.
    :param colors: List of colors to use for different columns.
    :param file_name: The name of the file to save the plot as.
    """
    num_rows, num_columns = data.shape
    x = np.arange(num_rows)  # Label positions
    width = graph_config.BAR_WIDTH

    # Dynamically adjust figure size
    fig_width = max(graph_config.WIDTH, num_columns * 1.2)  # Scale width based on columns
    fig_height = max(graph_config.HEIGHT, num_rows * 0.5)  # Scale height based on rows
    fig, ax = plt.subplots(figsize=(fig_width, fig_height), layout='constrained')

   # Plot bars
    for i, column in enumerate(data.columns):
        offset = (i - (num_columns - 1) / 2) * width  # Center bars
        rects = ax.bar(x + offset, data[column], width, label=column, color=graph_config.COLOR_THEME[i % len(graph_config.COLOR_THEME)])
        ax.bar_label(rects, padding=3)

    # Set labels and title with font size
    ax.set_ylabel(graph_config.Y_AXIS, fontsize=graph_config.AXIS_LABEL_FONT_SIZE)
    ax.set_title(graph_config.TITLE, fontsize=graph_config.TITLE_SIZE)
    ax.set_xticks(x)
    ax.set_xticklabels(data.index, fontsize=graph_config.AXIS_LABEL_FONT_SIZE)
    ax.legend(loc="upper left", ncol=min(num_columns, 3))

    # Adjust y-axis dynamically
    ax.set_ylim(0, data.max().max() * 1.1)

    # Grid for readability
    ax.grid(True, axis='y', linestyle='--', alpha=0.4)

    # Save the graph
    save_graphs(plt, file_name)