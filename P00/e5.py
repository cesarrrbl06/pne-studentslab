from seq0 import *


genes = ["U5", "FRAT1", "FXN", "ADA"]

print("-----| Exercise 5 |------")
for gene in genes:
    seq = seq_read_fasta(f"{gene}.txt")
    base_counts = seq_count_bases(seq)
    print(f"Gene {gene}: {base_counts}\n")

