import os
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator

from globals import ColorPalette, Const
from handle_data import get_files_list, load_data_matrix_format, save_graphs

class PlotConsts:
    # Define constants for plot customization
    Y_NBINS = 20

    # Axis labels
    X_LABEL = ''
    Y_LABEL = ''

    # Plot title - the default is the file name (if you prefer this do not change)
    TITLE = ''

    # Plot colors (example: use ColorPalette from existing colors)
    COLORS = ColorPalette.BASIC_THEME

def generate_graph(args):
    """
    Plots the data from the DataFrame with dots and connecting lines for each file.
    Uses constants for plot customization like labels, colors, and title.
    """

    # If input is a directory, get all files inside
    files = get_files_list(args)

    for file in files:
        plt.figure(figsize=(Const.WIDTH, Const.HEIGHT)) 
        data = load_data_matrix_format(file)

        # Extract filename without extension
        file_name_without_extension = os.path.splitext(os.path.basename(file))[0]

        # Use the first column as X-axis
        x_axis = data.iloc[:, 0]
        
        # Loop through the rest of the columns as Y-axes
        for i in range(1, data.shape[1]):  
            y_axis = data.iloc[:, i]
            y_label = data.columns[i]  # Default y-label from column name
            color = PlotConsts.COLORS[i % len(PlotConsts.COLORS)]  # Cycle through colors
            plt.plot(x_axis, y_axis, marker='o', linestyle='-', label=y_label, color=color)

        # Turn off scientific notation and use plain numbers
        plt.ticklabel_format(style='plain', axis='both')

        # Increase resolution by adding more y-axis ticks
        plt.gca().yaxis.set_major_locator(MaxNLocator(integer=True, nbins=PlotConsts.Y_NBINS))

        # Set title with optional LABEL prefix
        plt.title(PlotConsts.TITLE if PlotConsts.TITLE else f"{file_name_without_extension}".strip())

        # Set labels
        plt.xlabel(PlotConsts.X_LABEL if PlotConsts.X_LABEL else data.columns[0])
        plt.ylabel(PlotConsts.Y_LABEL if PlotConsts.Y_LABEL else '')
        plt.legend()
        plt.grid()

        # Save the graph
        save_graphs(plt, file_name_without_extension)

