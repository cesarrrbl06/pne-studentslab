from pathlib import Path
filename = "sequences/Felis_catus_FXN_sequence.txt"
file_contents = Path(filename).read_text()
list_contents = file_contents.split('\n')

list_contents.pop(0)
print(len(''.join(list_contents)))
