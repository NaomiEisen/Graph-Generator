import pandas as pd
import io

text = """\
           0         1         2         3         4         5         6         7
 0      1.11      1.11      1.11      0.40      0.40      0.39      0.39      1.11
"""

# Remove leading/trailing spaces and split into lines
lines = text.strip().split("\n")

# Extract header and remove leading spaces
headers = lines[0].split()

# Extract data and ignore the first value in each row (index)
data_lines = [line.split()[1:] for line in lines[1:]]

# Convert to Pandas DataFrame
df = pd.DataFrame(data_lines, columns=headers)

# Convert data to float
df = df.astype(float)

print(df)