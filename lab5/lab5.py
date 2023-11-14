import sys
import json
from functools import reduce

def remove_output(cell):
    if cell['cell_type'] == 'code':
        cell['outputs'] = []

def remove_code_after_markdown(cell1, cell2): #funkcja niestety nie działa :(
    if(cell1['cell_type'] == 'markdown'
            and "Ćwiczenie" in cell1['source'] and cell2['cell_type'] == 'code'):
        cell2['source'] = []
    return cell2

input_file = sys.argv[1]
output_file = input_file.replace(".ipynb", ".clean.ipynb")
with open(sys.argv[1]) as f:
    file = json.load(f)

#usuwanie policzonych wartości z komórek typu 'code'
l = list(map(remove_output, file['cells']))

#usuwanie kodu z komórek typu 'code'
result = reduce(remove_code_after_markdown, file["cells"])

with open(output_file, 'w') as f:
    json.dump(file, f)

print(f"Plik {output_file} został zapisany.")
