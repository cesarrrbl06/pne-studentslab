from Seq1 import Seq
from pathlib import Path


class MySeq(Seq):
    def __init__(self, filename):
        strbases = self.seq_read_fasta(filename)
        super().__init__(strbases)
        if not all(base in 'ACTG' for base in strbases):
            print("INVALID sequence!")
            self.strbases = "ERROR"
        elif len(strbases) == 0:
            print("NULL sequence created")
            self.strbases = "NULL"
        else:
            print("New sequence created!")
        self.count_bases()

    def seq_read_fasta(self, filename):
        file_contents = Path(filename).read_text()
        list_contents = file_contents.split('\n')
        dna_sequence = ''.join(list_contents[1:])  # Join all lines except the header
        return dna_sequence

    def count_bases(self):
        bases = ['A', 'C', 'T', 'G']
        self.bases_count = {base: self.strbases.count(base) for base in bases}

    def reverse(self):
        if self.strbases in ["NULL", "ERROR"]:
            return self.strbases
        else:
            return self.strbases[::-1]

    def complement(self):
        if self.strbases in ["NULL", "ERROR"]:
            return self.strbases
        else:
            complement_dict = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
            return ''.join([complement_dict[base] for base in self.strbases])

    def __str__(self):
        return self.strbases

    def len(self):
        return len(self.strbases)


print("-----| Practice 1, Exercise 9 |------")
seq1 = MySeq("U5.txt")

print(f"Sequence : (Length: {seq1.len()}) {seq1}")
print(f"  Bases: {seq1.bases_count}")
print(f"  Rev:   {seq1.reverse()}")
print(f"  Comp:  {seq1.complement()}")
