from Seq1 import *
from pathlib import Path

print("-----| Practice 1, Exercise 9 |------")
seq1 = MySeq("U5.txt")

print(f"Sequence : (Length: {seq1.len()}) {seq1}")
print(f"  Bases: {seq1.bases_count}")
print(f"  Rev:   {seq1.reverse()}")
print(f"  Comp:  {seq1.complement()}")
