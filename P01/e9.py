from Seq1 import *

print("-----| Practice 1, Exercise 9 |------")
seq = Seq("U5.txt")

print(f"Sequence : (Length: {seq.len()}) {seq}")
print(f"  Bases: {seq.bases_count}")
print(f"  Rev:   {seq.seq_reverse()}")
print(f"  Comp:  {seq.seq_complement()}")
