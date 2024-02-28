from seq0 import *
from Client0 import Client

genes = ["FRAT1"]
for gene in genes:
    seq = seq_read_fasta(f"{gene}.txt")


for i in seq:
