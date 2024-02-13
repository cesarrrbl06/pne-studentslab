from pathlib import Path
filename = "sequences/FXN.txt"
file_contents = Path(filename).read_text()
list_contents = file_contents.split('\n')

list_contents.pop(0)
print(len(''.join(list_contents)))
