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
        self.count_bases()

    def count_bases(self):
        bases = ['A', 'C', 'T', 'G']
        self.bases_count = {base: self.strbases.count(base) for base in bases}

    def __str__(self):
        return self.strbases

    def len(self):
        return len(self.strbases)

print("-----| Practice 1, Exercise 6 |------")
seq1 = MySeq("")
seq2 = MySeq("ACTGA")
seq3 = MySeq("TATXC")

for i, seq in enumerate([seq1, seq2, seq3], 1):
    print(f"Sequence {i}: (Length: {seq.len()}) {seq}")
    print(f"  Bases: {seq.bases_count}")
    print("\n")



