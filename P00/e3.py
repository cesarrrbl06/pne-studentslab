from seq0 import *

genes = ['U5', 'ADA', 'FRAT1', 'FXN']

for gene in genes:
    filename = gene + '.txt'
    sequence = seq_read_fasta(filename)
    gene_length = seq_len(sequence)
    print('The length of gene', gene, 'is:', gene_length)
