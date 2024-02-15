from seq0 import *

gene = "U5"
seq = seq_read_fasta(f"{gene}.txt")

fragment = seq[:20]
print(f"Fragment (first 20 bases of {gene}): {fragment}")

complementary = seq_complement(fragment)
print(f"The complementary is {complementary}")

