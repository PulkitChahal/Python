import nbformat
import os


def merge_notebooks(input_files, output_file):
    # Initialize a new notebook
    merged_notebook = nbformat.v4.new_notebook()
    merged_notebook.cells = []

    # Loop through all input files and add their cells to the merged notebook
    for file in input_files:
        with open(file, "r", encoding="utf-8") as f:
            notebook = nbformat.read(f, as_version=4)
            merged_notebook.cells.extend(notebook.cells)

    # Write the merged notebook to the output file
    with open(output_file, "w", encoding="utf-8") as f:
        nbformat.write(merged_notebook, f)


path = r'C:\Users\pulki\Python'
input_files = [file for file in os.listdir(path) if file.endswith(".ipynb")]
output_file = "Advanced_Python.ipynb"
print(input_files)

# merge_notebooks(input_files, output_file)
