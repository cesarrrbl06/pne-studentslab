from Seq1 import Seq
from pathlib import Path

class MySeq(Seq):
    def __init__(self, filename):
        strbases = self.seq_read_fasta(filename)
        if len(strbases) == 0:
            print("NULL sequence created")
            self.strbases = "NULL"
        else:
            super().__init__(strbases)
            self.count_bases()

    def seq_read_fasta(self, filename):
        file_contents = Path(filename).read_text()
        list_contents = file_contents.split('\n')
        dna_sequence = ''.join(list_contents[1:])  # Join all lines except the header
        return dna_sequence

    def count_bases(self):
        bases = ['A', 'C', 'T', 'G']
        self.bases_count = {base: self.strbases.count(base) for base in bases}

    def most_frequent_base(self):
        return max(self.bases_count, key=self.bases_count.get)


genes = ["U5", "ADA", "FRAT1", "FXN"]
print("-----| Practice 1, Exercise 10 |------")
for gene in genes:
    seq = MySeq(f"{gene}.txt")
    if seq.strbases != "NULL":
        print(f"Gene {gene}: Most frequent Base: {seq.most_frequent_base()}")

