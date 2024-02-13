def seq_ping():
    print("OK")


from pathlib import Path


def seq_read_fasta(filename):
    file_contents = Path(filename).read_text()
    list_contents = file_contents.split('\n')
    dna_sequence = ''.join(list_contents[1:])  # Join all lines except the header
    return dna_sequence


filename = "U5.txt"
dna_sequence = seq_read_fasta(filename)
print(dna_sequence)
