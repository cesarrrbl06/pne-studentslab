from pathlib import Path

filename = "sequence/Felis_catus_FXN_sequence.txt"
file_contents = Path(filename).read_text()
list_contents = file_contents.split("\n")
print(list_contents[0])