import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

from data_structures.nv_bandwidth_struct import NvBandwidth
from graph_generators.gradient_bars import gradient_bars
from utils.colors import ColorPalette
from utils.handle_data import save_graphs

def org_vs_opt_bar_graph_nvbandwidth(data_org, data_opt, graph_config, file_name, test_name):
    if list(data_org.columns) != list(data_opt.columns):
        raise ValueError("data_org and data_opt must have the same columns")

    if len(data_org.columns) == 1:
        plot_four_graphs_opt_vs_org(data_org, data_opt, graph_config, file_name, test_name)
    else:
        x = np.arange(len(data_org.columns))

        # Create the plot
        fig, ax = plt.subplots()

        # Plot the bars
        rect1 = ax.bar(x - graph_config.BAR_WIDTH / 2 - 0.01, data_org.mean(), graph_config.BAR_WIDTH)
        gradient_bars(rect1, NvBandwidth.TYPE_ORG)
        rect2 = ax.bar(x + graph_config.BAR_WIDTH / 2 + 0.01, data_opt.mean(), graph_config.BAR_WIDTH)
        gradient_bars(rect2, NvBandwidth.TYPE_OPT)

        ax.bar_label(rect1, padding=3, fontsize=graph_config.BAR_LABEL_FONT_SIZE)
        ax.bar_label(rect2, padding=3, fontsize=graph_config.BAR_LABEL_FONT_SIZE)

        ax.set_xticks(x)
        ax.set_xticklabels(['GPU' + str(x_val) for x_val in x])
        ax.set_xlabel(graph_config.X_AXIS)

        ax.set_ylabel(graph_config.Y_AXIS)
        ax.set_title(test_name)

        # Extend the axes-limit to make room for the legend
        ax.set_ylim(0, max(data_org.max().max(), data_opt.max().max()) * 1.2)
        ax.set_xlim(-1, len(data_org.columns))

        ax.legend(handles = [
            mpatches.Patch(color=ColorPalette.COLOR_THEME_OPT_VS_ORG[NvBandwidth.TYPE_ORG]['start'], label='Original xml'),
            mpatches.Patch(color=ColorPalette.COLOR_THEME_OPT_VS_ORG[NvBandwidth.TYPE_OPT]['start'], label ='Optimal xml')
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

            ax[i, j].bar_label(bar_org, padding=3, fontsize=graph_config.BAR_LABEL_FONT_SIZE-4)
            ax[i, j].bar_label(bar_opt, padding=3, fontsize=graph_config.BAR_LABEL_FONT_SIZE-4)

            ax[i, j].set_ylim(y_min, y_max)  # Set the same y-axis range
            ax[i, j].set_title(data_org.index[idx])  # Title as row name
            ax[i, j].set_ylabel(graph_config.Y_AXIS)

            ax[i, j].set_xlim(0, x_range)  # Set x range
            ax[i, j].tick_params(axis='x', bottom=False, labelbottom=False)  # Remove x-ticks

            ax[i, j].grid(True)
            gradient_bars(bar_org, NvBandwidth.TYPE_ORG)
            gradient_bars(bar_opt, NvBandwidth.TYPE_OPT)

            idx += 1

    fig.legend(handles=[
        mpatches.Patch(color=ColorPalette.COLOR_THEME_OPT_VS_ORG[NvBandwidth.TYPE_ORG]['start'], label='Original xml'),
        mpatches.Patch(color=ColorPalette.COLOR_THEME_OPT_VS_ORG[NvBandwidth.TYPE_OPT]['start'], label='Optimal xml')
    ])
    fig.suptitle(test_name, fontsize=graph_config.TITLE_SIZE)

    # Save the graph without clipping issues
    save_graphs(plt, file_name)
    plt.close(fig)



