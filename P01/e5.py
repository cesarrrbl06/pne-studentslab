

from Seq1 import Seq

class MySeq(Seq):
    def __init__(self, strbases):
        self.strbases = strbases  # Do not call Seq's __init__ method
        if not all(base in 'ACTG' for base in strbases):
            print("INVALID sequence!")
            self.strbases = "ERROR"
        elif len(strbases) == 0:
            print("NULL sequence created")
            self.strbases = "NULL"
        else:
            print("New sequence created!")

    def __str__(self):
        return self.strbases

    def len(self):
        return len(self.strbases)

print("-----| Practice 1, Exercise 5 |------")
seq1 = MySeq("")
seq2 = MySeq("ACTGA")
seq3 = MySeq("TATXC")

for i, seq in enumerate([seq1, seq2, seq3], 1):
    print(f"Sequence {i}: (Length: {seq.len()}) {seq}")
    for base in ['A', 'C', 'T', 'G']:
        print(f"  {base}: {seq.strbases.count(base)}", end=",")
    print("\n")




