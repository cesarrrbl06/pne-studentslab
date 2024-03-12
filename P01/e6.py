from Seq1 import *

print("-----| Practice 1, Exercise 6 |------")
seq1 = Seq("")
seq2 = Seq("ACTGA")
seq3 = Seq("TATXC")

for i, seq in enumerate([seq1, seq2, seq3], 1):
    print(f"Sequence {i}: (Length: {seq.len()}) {seq}")
    print(f"  Bases: {seq.bases_count}")
    print("\n")



