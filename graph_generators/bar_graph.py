import matplotlib.pyplot as plt
import numpy as np

from utils.handle_data import save_graphs



def plot_bar_graph(data, graph_config, file_name, test_name):
    """
    Plots a Grafana-style bar graph from a Pandas DataFrame.
    Dark mode.
    """
    num_rows, num_columns = data.shape
    x = np.arange(num_rows)  # Label positions

    fig, ax = plt.subplots(figsize=(graph_config.WIDTH, graph_config.HEIGHT), facecolor="#1E1E1E", layout="constrained")

    # Apply Grafana-style aesthetics
    ax.set_facecolor("#1E1E1E")  # Dark background
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.spines["left"].set_color("white")
    ax.spines["bottom"].set_color("white")
    ax.tick_params(colors="white", labelsize=graph_config.AXIS_LABEL_FONT_SIZE)

    # Plot bars
    for i, column in enumerate(data.columns):
        offset = (i - (num_columns - 1) / 2) * graph_config.BAR_WIDTH  # Center bars
        rects = ax.bar(
            x + offset, data[column], graph_config.BAR_WIDTH,
            label=column, color=graph_config.COLOR_THEME[i % len(graph_config.COLOR_THEME)]
        )
        ax.bar_label(rects, padding=3, fontsize=graph_config.BAR_LABEL_FONT_SIZE, color="white")

    # Set labels and title with font size
    ax.set_ylabel(graph_config.Y_AXIS, fontsize=graph_config.AXIS_LABEL_FONT_SIZE, color="white")
    ax.set_title(test_name, fontsize=graph_config.TITLE_SIZE, color="white")
    ax.set_xticks(x)
    ax.set_xticklabels(data.index, fontsize=graph_config.AXIS_LABEL_FONT_SIZE, color="white")
    ax.legend(loc="upper left", ncol=min(num_columns, 3), facecolor="#1E1E1E", framealpha=1, fontsize=graph_config.LEGEND_FONT_SIZE, labelcolor="white")

    # Adjust y-axis dynamically
    ax.set_ylim(0, data.max().max() * 1.1)
    
    # Grid for readability
    ax.grid(True, axis='y', linestyle="--", linewidth=0.5, color="gray", alpha=0.5)

    # Automatically adjust layout
    plt.tight_layout()

    # Save the graph without clipping issues
    save_graphs(plt, file_name)
    plt.close(fig)