import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

from data_structures.test_verion import TestVersion
from graph_generators.gradient_bars import gradient_bars
from utils.colors import ColorPalette
from utils.general import save_graphs


def comparison_bar_graph_nvbandwidth(data_v1, data_v2, graph_config, file_name, test_name):
    if list(data_v1.columns) != list(data_v2.columns):
        raise ValueError("data_org and data_opt must have the same columns")

    if len(data_v1.columns) == 1:
        plot_four_graphs_opt_vs_org(data_v1, data_v2, graph_config, file_name, test_name)
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

        ax.legend(handles = [
            mpatches.Patch(color=ColorPalette.COLOR_THEME_COMPARISON[TestVersion.V1]['start'], label=graph_config.V1_LEGEND),
            mpatches.Patch(color=ColorPalette.COLOR_THEME_COMPARISON[TestVersion.V2]['start'], label =graph_config.V2_LEGEND)
        ])

        save_graphs(plt, file_name)

def plot_four_graphs_opt_vs_org(data_org, data_opt, graph_config, file_name, test_name):
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

    fig.legend(handles=[
        mpatches.Patch(color=ColorPalette.COLOR_THEME_COMPARISON[TestVersion.V1]['start'], label=graph_config.V1_LEGEND),
        mpatches.Patch(color=ColorPalette.COLOR_THEME_COMPARISON[TestVersion.V2]['start'], label=graph_config.V2_LEGEND)
    ])
    fig.suptitle(test_name, fontsize=graph_config.TITLE_SIZE)

    # Save the graph without clipping issues
    save_graphs(plt, file_name)
    plt.close(fig)