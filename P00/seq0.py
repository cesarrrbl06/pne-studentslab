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


def seq_len(seq):
    return len(seq)


def seq_count_base(seq, base):
    return seq.count(base)


def seq_count_bases(seq):
    bases = ['A', 'T', 'C', 'G']
    base_counts = {base: seq.count(base) for base in bases}
    return base_counts


def seq_reverse(seq, n):
    return seq[:n][::-1]


def seq_complement(seq):
    complement = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
    return ''.join([complement[base] for base in seq])
