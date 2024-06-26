from seq0 import *
gene = "U5"
seq = seq_read_fasta(f"{gene}.txt")

fragment = seq[:20]
print(f"Fragment (first 20 bases of {gene}): {fragment}")

reverse_fragment = seq_reverse(fragment, len(fragment))
print(f"Reverse of fragment: {reverse_fragment}")