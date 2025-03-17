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
  ![#4394E5](https://via.placeholder.com/20/4394E5/000000?text=+) ![#F5921B](https://via.placeholder.com/20/F5921B/000000?text=+) ![#5E40BE](https://via.placeholder.com/20/5E40BE/000000?text=+) ![#87BB62](https://via.placeholder.com/20/87BB62/000000?text=+) ![#D46FAD](https://via.placeholder.com/20/D46FAD/000000?text=+)

- **Sunset Theme**:  
  ![#003F5C](https://via.placeholder.com/20/003F5C/000000?text=+) ![#58508D](https://via.placeholder.com/20/58508D/000000?text=+) ![#BC5090](https://via.placeholder.com/20/BC5090/000000?text=+) ![#FF6361](https://via.placeholder.com/20/FF6361/000000?text=+) ![#FFA600](https://via.placeholder.com/20/FFA600/000000?text=+)

- **Retro Theme**:  
  ![#780C28](https://via.placeholder.com/20/780C28/000000?text=+) ![#6E8E59](https://via.placeholder.com/20/6E8E59/000000?text=+) ![#DF6D14](https://via.placeholder.com/20/DF6D14/000000?text=+)

- **Earth Theme**:  
  ![#27445D](https://via.placeholder.com/20/27445D/000000?text=+) ![#497D74](https://via.placeholder.com/20/497D74/000000?text=+) ![#A0C878](https://via.placeholder.com/20/A0C878/000000?text=+)

- **Girly Theme**:  
  ![#69247C](https://via.placeholder.com/20/69247C/000000?text=+) ![#DA498D](https://via.placeholder.com/20/DA498D/000000?text=+) ![#FAC67A](https://via.placeholder.com/20/FAC67A/000000?text=+)
