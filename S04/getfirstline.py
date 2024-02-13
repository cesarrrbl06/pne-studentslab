from pathlib import Path

filename = "sequences/FXN.txt"
file_contents = Path(filename).read_text()
list_contents = file_contents.split('\n')
print(list_contents[0])