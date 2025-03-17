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
  <span style="background-color:#4394E5;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span> <span style="background-color:#F5921B;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span> <span style="background-color:#5E40BE;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span> <span style="background-color:#87BB62;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span> <span style="background-color:#D46FAD;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

- **Sunset Theme**:  
  <span style="background-color:#003F5C;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span> <span style="background-color:#58508D;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span> <span style="background-color:#BC5090;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span> <span style="background-color:#FF6361;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span> <span style="background-color:#FFA600;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

- **Retro Theme**:  
  <span style="background-color:#780C28;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span> <span style="background-color:#6E8E59;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span> <span style="background-color:#DF6D14;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

- **Earth Theme**:  
  <span style="background-color:#27445D;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span> <span style="background-color:#497D74;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span> <span style="background-color:#A0C878;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

- **Girly Theme**:  
  <span style="background-color:#69247C;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span> <span style="background-color:#DA498D;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span> <span style="background-color:#FAC67A;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>
