import matplotlib.pyplot as plt
import numpy as np

from graph_generators.gradient_bars import gradient_bars
from utils.handle_data import save_graphs


def plot_bar_graph(data, graph_config, file_name, test_name, test_type = 0):
    num_rows, num_columns = data.shape
    if num_rows == 4 and num_columns == 1:
        plot_four_graphs(data, graph_config, file_name, test_name)
        return

    fig, ax = plt.subplots()
    x = np.arange(num_columns) # Label positions

    # Plot bars
    for i, column in enumerate(data.columns):
        bar = ax.bar(i, data[column], width=graph_config.BAR_WIDTH, label=column)
        ax.bar_label(bar, padding=3, fontsize=graph_config.BAR_LABEL_FONT_SIZE)
        gradient_bars(bar, test_type)

    ax.set_xticks(x)  # Center ticks at group positions
    plt.xlim(-1, num_columns)
    ax.set_xticklabels(data.columns)

    # create more space for legend by increasing the y axes range
    ax.set_ylabel(graph_config.Y_AXIS)
    ax.set_title(test_name)

    # Grid for readability
    ax.grid(True)

    # Save the graph without clipping issues
    save_graphs(plt, file_name)
    plt.close(fig)

def plot_four_graphs(data, graph_config, file_name, test_name, test_type = 0):
    fig, ax = plt.subplots(2, 2, figsize=(30,15))
    x = [1]

    print(data)
    # Get global min and max for the y-axis range
    y_min = 0 # Minimum of the first columns
    y_max = data.iloc[:, 0].max() + 50  # Maximum of the first column

    # Plot each data point in its respective subplot
    idx = 0
    for i in range(2):  # Row index
        for j in range(2):  # Column index
            bar = ax[i, j].bar(x,  data.iloc[idx, 0],  width=0.15, bottom=None, align='center'
                               ,edgecolor= 'white', label=data.columns[0] )
            ax[i, j].bar_label(bar, padding=3, fontsize=graph_config.BAR_LABEL_FONT_SIZE)
            ax[i, j].set_ylim(y_min, y_max)  # Set the same y-axis range
            ax[i, j].set_xlim(0, 2)  # Set x range
            ax[i, j].tick_params(axis='x', bottom=False, labelbottom=False)  # Remove x-ticks
            ax[i, j].set_title(data.index[idx])  # Title as row name
            ax[i,j].set_ylabel(graph_config.Y_AXIS)
            ax[i,j].grid(True)
            gradient_bars(bar, test_type)

            idx += 1

    handles, labels = ax[0, 0].get_legend_handles_labels()  # Extract handles and labels
    fig.legend(handles, [data.columns[0]], loc="lower left")

    fig.suptitle(test_name, fontsize=graph_config.TITLE_SIZE)


    # Save the graph without clipping issues
    save_graphs(plt, file_name)
    plt.close(fig)


# def plot_bar_graph_old(data, graph_config, file_name, test_name, test_type = 0):
#     num_rows, num_columns = data.shape
#     if num_rows == 4 and num_columns == 1:
#         plot_four_graphs(data, graph_config, file_name, test_name)
#         return
#
#     fig, ax = plt.subplots()
#     x = np.arange(num_rows)  # Label positions
#
#     # Plot bars
#     for i, column in enumerate(data.columns):
#         offset = (i - 2) * (graph_config.BAR_WIDTH + 0.1)
#         rects = ax.bar(x+ offset, data[column], width=graph_config.BAR_WIDTH, label=column,
#               color=graph_config.COLOR_THEME[test_type%2][i % len(graph_config.COLOR_THEME)])
#         ax.bar_label(rects, padding=3, fontsize=graph_config.BAR_LABEL_FONT_SIZE)
#
#     ax.set_xticks(x+0.3)  # Center ticks at group positions
#
#
#     # create more space for legend by increasing the y axes range
#     ax.set_ylim(0, data.max().max() * 1.3)
#     ax.set_ylabel(graph_config.Y_AXIS)
#     ax.set_title(test_name)
#     ax.legend(loc="upper left", ncol=min(num_columns, 3))
#
#     # Grid for readability
#     ax.grid(True)
#
#     # Save the graph without clipping issues
#     save_graphs(plt, file_name)
#     plt.close(fig)