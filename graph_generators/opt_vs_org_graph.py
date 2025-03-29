import matplotlib.pyplot as plt
import numpy as np

from utils.handle_data import save_graphs

LIGHT_BLUE = "#00D4B5"
MEDIUM_BLUE = '#00A5B5'
LIGHT_PINK = '#EB859A'
MEDIUM_PINK = '#E0516D'
LIGHT_GREEN = '#B7CD67'
MEDIUM_GREEN = '#8DC72B'
LIGHT_ORANGE = "#E69500"
MEDIUM_ORANGE = '#F0A95A'

def org_vs_opt_bar_graph(data_org, data_opt, graph_config, file_name, test_name):
    if list(data_org.columns) != list(data_opt.columns):
        raise ValueError("data_org and data_opt must have the same columns")

    if len(data_org.columns) == 1:
        plot_one_column_data(data_org, data_opt, graph_config, file_name, test_name)
    else:
        x = np.arange(len(data_org.columns))

        # Create the plot
        fig, ax = plt.subplots()

        # Plot the bars
        rect1 = ax.bar(x - graph_config.BAR_WIDTH / 2, data_org.mean(), graph_config.BAR_WIDTH, label='Original xml',
                   color=LIGHT_BLUE)
        rect2 = ax.bar(x + graph_config.BAR_WIDTH / 2, data_opt.mean(), graph_config.BAR_WIDTH, label = 'Optimal xml', color = LIGHT_ORANGE)

        ax.bar_label(rect1, padding=3, fontsize=graph_config.BAR_LABEL_FONT_SIZE)
        ax.bar_label(rect2, padding=3, fontsize=graph_config.BAR_LABEL_FONT_SIZE)

        ax.set_xticks(x)
        ax.set_xticklabels(['GPU' + str(x_val) for x_val in x])
        ax.set_xlabel(graph_config.X_AXIS)

        ax.set_ylabel(graph_config.Y_AXIS)
        ax.set_title(test_name)

        # Extend the y-limit to make room for the legend
        ax.set_ylim(0, max(data_org.max().max(), data_opt.max().max()) * 1.2)
        ax.legend()

        save_graphs(plt, file_name)

def plot_one_column_data(data_org, data_opt, graph_config, file_name, test_name):

    x = np.arange(6)

    # Create the plot
    fig, ax = plt.subplots()

    # Plot the bars
    rect1 = ax.bar(2, data_org.mean(), 0.4, label='Original xml',
                   color=LIGHT_BLUE)
    rect2 = ax.bar(3,data_opt.mean(), 0.4, label='Optimal xml',
                   color=LIGHT_ORANGE)

    ax.bar_label(rect1, padding=3, fontsize=graph_config.BAR_LABEL_FONT_SIZE)
    ax.bar_label(rect2, padding=3, fontsize=graph_config.BAR_LABEL_FONT_SIZE)

    ax.set_xticks(x)
    ax.tick_params(axis='x', labelbottom=False)
    ax.set_xlabel(graph_config.X_AXIS)

    ax.set_ylabel(graph_config.Y_AXIS)
    ax.set_title(test_name)

    # Extend the y-limit to make room for the legend
    ax.set_ylim(0, max(data_org.max().max(), data_opt.max().max()) * 1.2)
    ax.legend()
    save_graphs(plt, file_name)


# x = np.linspace(0, 10, 100)
#
# fig, ax = plt.subplots(2, 2)  # Creates a 2x2 grid of subplots
#
# ax[0, 0].plot(x, np.sin(x))  # Top-left subplot
# ax[0, 1].plot(x, np.cos(x))  # Top-right subplot
# ax[1, 0].plot(x, np.tan(x))  # Bottom-left subplot
# ax[1, 1].plot(x, np.exp(-x))  # Bottom-right subplot
