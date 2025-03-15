import os
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator

from globals import ColorPalette, Const
from handle_data import load_data_matrix_format, get_files_list, save_graphs


class PlotConsts:
    Y_NBINS = 20  # Number of bins on the y-axis

    # List of colors for multiple lines
    COLORS = ColorPalette.BASIC_THEME



def customize():
    # Ask if the user wants to customize the plot
    customize_choice = input("Do you want to customize the plot? (y/n): ").lower()

    if customize_choice == 'y':
        # Ask for Y-axis label
        y_label = input("Enter Y-axis label: ")

        # Ask for X-axis label
        x_label = input("Enter X-axis label: ")

        # Ask for title
        title = input("Enter plot title: ")

        # Define theme options in a dictionary
        themes = {
            '1': 'Sunset',
            '2': 'Retro',
            '3': 'Earth',
            '4': 'Girly',
            '5': 'Basic Color Palette'
        }

        # Ask for theme selection
        print("Choose a color theme:")
        for key, value in themes.items():
            print(f"{key}. {value}")

        theme_choice = input("Enter the number corresponding to the theme: ")

        # Get the selected theme or default to 'Basic Color Palette' if invalid
        theme = themes.get(theme_choice, 'Basic Color Palette')

        # Return the customizations as a dictionary
        return y_label, x_label, title
    
    else:
        print("Customization skipped.")
        # Return an empty dictionary with default values
        return '','',''


def plot_data_from_files(args):
    """
    Loads the data from multiple files and plots them separately:
    - Each file generates a separate plot.
    - The first column is used as the X-axis.
    - Each remaining column is plotted as a separate Y-axis.
    - Labels are taken from the column headers.
    - The title is PlotConsts.TITLE + filename (without extension).
    """
    y_axiss_label, x_axis_label, title = customize()
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
        plt.title(title if title else f"{file_name_without_extension}".strip())

        # Labels
        plt.xlabel(x_axis_label if x_axis_label else data.columns[0])
        plt.ylabel(y_axiss_label if y_axiss_label else "")  # Use custom y-label if set
        plt.legend()
        plt.grid()

        # Save the graph
        save_graphs(plt, file_name_without_extension)
