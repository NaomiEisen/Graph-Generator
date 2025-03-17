# Graph-Generator
A tool for generating graphs from matrix-formatted data (e.g., Excel or TXT files), featuring customizable templates for graph creation (and personal generators for specific tests).

## How to Run the Program

To run the Graph Generator, follow these steps:

### 1. Clone the Repository

Clone the repository to your local machine using Git:

```bash
git clone <repository-url>
cd <repository-name>
```

### 2. Install Required Dependencies
Install the necessary Python dependencies using <pip>:

```bash
pip install matplotlib pandas openpyxl
```

### 3. Run the Program
Run the generator by executing the following command in the terminal:

Run the generator by executing the following command in the terminal:
```bash
python <generator-name> <file-paths>
```
- Replace <generator-name> with the name of the generator script you'd like to run.
- <file-paths> can either be individual file paths or a directory path containing the files.

### 4. Customize the Graph (Optional)

After running the program, you will be prompted to customize the graph. The options available are:

-Title: Set the title of your graph.
-Axis Labels: Customize the X-axis and Y-axis labels.
-Color Theme: Choose a color theme for the graph.
If you select "yes" for customization, you will be able to adjust these parameters.

### 5.  Output Location

The generated graphs will be saved in the output-graphs folder.

## Input Format

The input file can be in either `.txt` or `.xlsx` format. The structure is the same for both:

| x_axis_label  | y_axis1_label  | y_axis2_label  | ... |
|---------------|----------------|----------------|-----|
| x1_value      | y11_value      | y21_value      | ... |
| x2_value      | y12_value      | y22_value      | ... |
| ...           | ...            | ...            | ... |
| xn_value      | y1n_value      | y2n_value      | ... |

- The first column represents the **X-axis values**.
- The subsequent columns represent different **Y-axis values**.


## How to Add Your Own Graph Generator

If the provided graph generators do not meet your needs, you can easily add your own! (Or, perhaps you can just examine the results on your own without generating a graph, as some of us might suggest it could be a more appropriate approach.) Here's how:

1. Edit the Template: A template for creating new graph generators is provided in the empty-template.py file. You can edit this file to suit your needs.
2. Update the Globals File: Add the name of your custom graph generator to the globals.py file to make it available for use in the project.
3. Link the Generator: In the create_graph.py file, locate the marked section and add the function for your custom generator. This will allow the program to navigate to the initial function of your custom graph generator.

### Themed Color Sets

- **Basic Theme**:  
  <div style="display: flex; flex-wrap: wrap;">
    <img src="https://www.colorhexa.com/4394e5.png" width="30" height="30" alt="Vivid Blue"> 
    <img src="https://www.colorhexa.com/f5921b.png" width="30" height="30" alt="Bright Orange">
    <img src="https://www.colorhexa.com/5e40be.png" width="30" height="30" alt="Strong Purple">
    <img src="https://www.colorhexa.com/87bb62.png" width="30" height="30" alt="Fresh Green">
    <img src="https://www.colorhexa.com/d46fad.png" width="30" height="30" alt="Soft Pink">
  </div>

- **Sunset Theme**:  
  <div style="display: flex; flex-wrap: wrap;">
    <img src="https://www.colorhexa.com/003f5c.png" width="30" height="30" alt="Deep Twilight Blue">
    <img src="https://www.colorhexa.com/58508d.png" width="30" height="30" alt="Dusk Purple">
    <img src="https://www.colorhexa.com/bc5090.png" width="30" height="30" alt="Vibrant Sunset Magenta">
    <img src="https://www.colorhexa.com/ff6361.png" width="30" height="30" alt="Fiery Red-Orange Sunset">
    <img src="https://www.colorhexa.com/ffa600.png" width="30" height="30" alt="Warm Golden Glow">
  </div>

- **Retro Theme**:  
  <div style="display: flex; flex-wrap: wrap;">
    <img src="https://www.colorhexa.com/780c28.png" width="30" height="30" alt="Deep Vintage Red">
    <img src="https://www.colorhexa.com/6e8e59.png" width="30" height="30" alt="Muted Olive Green">
    <img src="https://www.colorhexa.com/df6d14.png" width="30" height="30" alt="Warm Burnt Orange">
  </div>

- **Earth Theme**:  
  <div style="display: flex; flex-wrap: wrap;">
    <img src="https://www.colorhexa.com/27445d.png" width="30" height="30" alt="Deep Ocean Blue">
    <img src="https://www.colorhexa.com/497d74.png" width="30" height="30" alt="Forest Teal">
    <img src="https://www.colorhexa.com/a0c878.png" width="30" height="30" alt="Fresh Nature Green">
  </div>

- **Girly Theme**:  
  <div style="display: flex; flex-wrap: wrap;">
    <img src="https://www.colorhexa.com/69247c.png" width="30" height="30" alt="Bold Feminine Purple">
    <img src="https://www.colorhexa.com/da498d.png" width="30" height="30" alt="Bright Pink">
    <img src="https://www.colorhexa.com/fac67a.png" width="30" height="30" alt="Soft Golden Peach">
  </div>

