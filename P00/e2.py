
with open("U5.txt", "r") as file:
    lines = file.readlines()
    sequence = ''.join(lines[1:]).strip()

# Print the first 20 bases of the sequence
print("First 20 bases of the sequence:")
print(sequence[:20])



