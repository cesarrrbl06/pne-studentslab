i = 0
sequence = "0,1"
fiboseries1 = 0
fiboseries2 = 1
while i < 9:
    fseries3 = fiboseries2 + fiboseries1
    sequence += ","
    sequence += str(fseries3)
    i += 1
    fiboseries1 = fiboseries2
    fiboseries2 = fseries3
print(sequence, end = ".")
