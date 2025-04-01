import matplotlib.pyplot as plt
import numpy as np

from data_structures.test_verion import TestVersion
from graph_generators.gradient_bars import gradient_bars, update_legends_colorscheme
from utils.general import save_graphs


def comparison_bar_graph(data_v1, data_v2, graph_config, file_name, test_name):
    if list(data_v1.columns) != list(data_v2.columns):
        raise ValueError("data_org and data_opt must have the same columns")

    if len(data_v1.columns) == 1:
        comparision_bar_subgraphs(data_v1, data_v2, graph_config, file_name, test_name)

    else:
        x = np.arange(len(data_v1.columns))

        # Create the plot
        fig, ax = plt.subplots()

        # Plot the bars
        rect1 = ax.bar(x - graph_config.BAR_WIDTH / 2 - 0.01, data_v1.mean(), graph_config.BAR_WIDTH)
        gradient_bars(rect1, TestVersion.V1)
        rect2 = ax.bar(x + graph_config.BAR_WIDTH / 2 + 0.01, data_v2.mean(), graph_config.BAR_WIDTH)
        gradient_bars(rect2, TestVersion.V2)

        ax.bar_label(rect1, padding=3, fontsize=graph_config.BAR_LABEL_FONT_SIZE)
        ax.bar_label(rect2, padding=3, fontsize=graph_config.BAR_LABEL_FONT_SIZE)

        ax.set_xticks(x)
        ax.set_xticklabels(['GPU' + str(x_val) for x_val in x])
        ax.set_xlabel(graph_config.X_AXIS)

        ax.set_ylabel(graph_config.Y_AXIS)
        ax.set_title(test_name)

        # Extend the axes-limit to make room for the legend
        ax.set_ylim(0, max(data_v1.max().max(), data_v2.max().max()) * 1.2)
        ax.set_xlim(-1, len(data_v1.columns))

        update_legends_colorscheme(fig, graph_config)

        save_graphs(plt, file_name)

def comparision_bar_subgraphs(data_org, data_opt, graph_config, file_name, test_name):
    fig, ax = plt.subplots(2, 2, figsize=(30,15))
    x_range = 6

    # Get global min and max for the y-axis range
    y_min = 0  # Minimum of the first columns
    y_max =max(data_org.iloc[:, 0].max(),data_opt.iloc[:, 0].max())  + 50  # Maximum of the first column

    # Plot each data point in its respective subplot
    idx = 0
    for i in range(2):  # Row index
        for j in range(2):  # Column index
            bar_org = ax[i, j].bar(x_range/2 + graph_config.BAR_WIDTH/2 + 0.01 , data_org.iloc[idx, 0], width=graph_config.BAR_WIDTH,label=data_org.columns[0])
            bar_opt = ax[i, j].bar(x_range/2 - graph_config.BAR_WIDTH/2 - 0.01, data_opt.iloc[idx, 0], width=graph_config.BAR_WIDTH, label=data_opt.columns[0])

            ax[i, j].bar_label(bar_org, padding=3, fontsize=graph_config.BAR_LABEL_FONT_SIZE-2)
            ax[i, j].bar_label(bar_opt, padding=3, fontsize=graph_config.BAR_LABEL_FONT_SIZE-2)

            ax[i, j].set_ylim(y_min, y_max)  # Set the same y-axis range
            ax[i, j].set_title(data_org.index[idx])  # Title as row name
            ax[i, j].set_ylabel(graph_config.Y_AXIS)

            ax[i, j].set_xlim(0, x_range)  # Set x range
            ax[i, j].tick_params(axis='x', bottom=False, labelbottom=False)  # Remove x-ticks

            ax[i, j].grid(True)
            gradient_bars(bar_org, TestVersion.V1)
            gradient_bars(bar_opt, TestVersion.V2)

            idx += 1

    update_legends_colorscheme(fig, graph_config)

    # Save the graph without clipping issues
    save_graphs(plt, file_name)
    plt.close(fig)

def comparison_line_graph(data_v1, data_v2, graph_config, file_name, number_plots=2):
    fig, ax = plt.subplots(number_plots, constrained_layout=True)

    # Define X range (min=0, max from first column)
    x_min, x_max = (0, data_v1.iloc[:, 0].max())
    x_range = np.linspace(x_min, x_max, num=len(data_v1))  # Generate evenly spaced values

    color_counter = 1
    for p in range(number_plots):
        # Loop through Y columns (other than the first one)
        for i in range(1, data_v1.shape[1]//2+1):
            y1_axis = data_v1.iloc[:, color_counter]
            y2_axis = data_v2.iloc[:, color_counter]
            y1_label = data_v1.columns[i]+graph_config.V1_LEGEND
            y2_label = data_v2.columns[i]+graph_config.V2_LEGEND
            color1 = graph_config.COLOR_THEME[color_counter % len(graph_config.COLOR_THEME)]
            color2 = graph_config.COLOR_THEME[color_counter+1 % len(graph_config.COLOR_THEME)]
            ax[p].plot(x_range, y1_axis, marker='o', linestyle='-', label=y1_label, color=color1)
            ax[p].plot(x_range, y2_axis, marker='o', linestyle='-', label=y2_label, color=color2)
            color_counter += 1

        # Set x-axis limits
        ax[p].set_xlim(x_min, x_max)

        # Titles and labels
        ax[p].set_title(graph_config.SUB_PLOT_TITLE[p])
        ax[p].set_xlabel(graph_config.X_AXIS if graph_config.X_AXIS else data_v1.columns[0])
        ax[p].set_ylabel(graph_config.Y_AXIS[p])
        ax[p].legend()
        ax[p].grid()

    fig.suptitle(graph_config.TITLE, fontsize=graph_config.TITLE_SIZE)
    # Save the graph
    save_graphs(plt, file_name)
