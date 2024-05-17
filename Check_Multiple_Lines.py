from sys import displayhook
import pandas as pd

file_path = 'progressElements05.csv'  # Replace with the path to your CSV file
df = pd.read_csv(file_path, low_memory=False)


def has_multiple_lines(cell_value):
    if isinstance(cell_value, str):
        # Split the cell value into lines
        lines = cell_value.split("\n")
        # Check if there are more than one line
        return len(lines) > 1
    else:
        return False


mask = df["elementName"].apply(has_multiple_lines)

rows_with_multiple_lines = df[mask]

if rows_with_multiple_lines.empty:
    print("No rows with multiple lines in the 'elementName' column found.")
else:
    print(rows_with_multiple_lines)

    # displayhook(rows_with_multiple_lines)2    1