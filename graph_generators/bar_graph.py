from matplotlib import pyplot as plt
from globals import ColorPalette, Const
import pandas as pd


BAR_WIDTH = 0.8

def plot_bar_graph(data):
    """
    Plots a bar graph for the combined data with 4 sections, each representing a row.
    Each section will have 8 bars, one for each column.
    
    :param combined_data: The Pandas DataFrame containing the combined data.
    """
    # Ensure all data is numeric (convert non-numeric values to NaN and handle them)
    #data = data.apply(pd.to_numeric, errors='coerce')

    # Drop rows or columns with NaN values if needed
    data = data.dropna(axis=1, how='all')  # Drop columns with all NaN values
    data = data.dropna(axis=0, how='all')  # Drop rows with all NaN values

    # Set the figure size using constants from Const class
    plt.figure(figsize=(Const.WIDTH, Const.HEIGHT))

    # Define the color palette for each section (row)
    colors = ColorPalette.GIRLY_THEME * 2  # Repeat the palette to cover all 4 rows

    # Create the bar plot with colors from the GIRLY_THEME
    ax = data.plot(kind='bar', width=0.8, color=colors)

    # Set plot title and labels
    plt.title("Memory Copy Test Results", fontsize=14)
    plt.xlabel("Test Types", fontsize=12)
    plt.ylabel("Values", fontsize=12)

    # Rotate x-axis labels for better readability
    plt.xticks(rotation=45, ha='right')

    # Adjust layout to make sure everything fits well
    plt.tight_layout()

    # Display the graph
    plt.show()