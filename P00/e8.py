from seq0 import *


genes = ["U5", "ADA", "FRAT1", "FXN"]
print("---------Excercise 8---------")
for gene in genes:
    seq = seq_read_fasta(f"{gene}.txt")
    base_counts = seq_count_bases(seq)
    most_frequent_base = max(base_counts, key=base_counts.get)
    print(f"Most frequent base in {gene}: {most_frequent_base}")