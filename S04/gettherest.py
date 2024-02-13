from pathlib import Path


filename = "sequences/FXN.txt"

file_contents = Path(filename).read_text()
list_contents = file_contents.split('\n')

for i in range (1,len(list_contents)):
    print(list_contents[i])