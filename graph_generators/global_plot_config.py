from matplotlib import pyplot as plt


def set_costume_global_plot_settings():
    plt.rcParams.update({
        # ---------- Figure Settings ----------
        'figure.facecolor': '#1e1e1e',  # Dark background for the figure
        'figure.figsize': (20, 15),

        # ---------- Axes Settings ----------
        'axes.facecolor': '#1e1e1e',  # Dark gray background for the plot area
        'axes.edgecolor': 'white',  # White borders for the axes
        'axes.labelcolor': 'white',  # White color for axis labels
        'axes.titlesize': 30,
        'axes.titlepad': 20,
        'axes.labelsize': 25,  # Set font size of axis labels
        'axes.labelpad': 15,  # Increase padding for all axis labels

        # ---------- Tick Settings ----------
        'xtick.color': 'white',  # White ticks along the x-axis
        'ytick.color': 'white',  # White ticks along the y-axis
        'xtick.labelsize': 20,  # Font size for x-axis tick labels
        'ytick.labelsize': 20,  # Font size for y-axis tick labels

        # ---------- Grid Settings ----------
        'grid.color': '#444444',  # Gridline color
        'grid.alpha': 0.5,  # Make the gridlines slightly transparent

        # ---------- Line Settings ----------
        'lines.linewidth': 2,  # Thicker lines for better visibility
        'lines.color': 'white',  # Default line color (can be overridden)

        # ---------- Legend Settings ----------
        'legend.fontsize': 20,  # Font size for legend text
        'legend.loc': 'upper left',  # Position the legend at the upper-left

        # ---------- Text Settings ----------
        'text.color': 'white'  # White text for titles and annotations
    })