from pathlib import Path


class Seq:
    """A class for representing sequences"""

    def __init__(self, filename=None, strbases=None):
        if filename:
            strbases = self.seq_read_fasta(filename)
        if strbases is None:
            print("NULL sequence created!")
            self.strbases = "NULL"
        elif not all(base in "ACGT" for base in strbases):
            print("Invalid sequence created!")
            self.strbases = "ERROR"
        else:
            self.strbases = strbases
            self.count_bases()

    def seq_read_fasta(self, filename):
        file_contents = Path(filename).read_text()
        list_contents = file_contents.split('\n')
        dna_sequence = ''.join(list_contents[1:])  # Join all lines except the header
        return dna_sequence

    def count_bases(self):
        if self.strbases not in ["NULL", "ERROR"]:
            bases = ['A', 'C', 'T', 'G']
            self.bases_count = {base: self.strbases.count(base) for base in bases}

    def most_frequent_base(self):
        if self.strbases not in ["NULL", "ERROR"]:
            return max(self.bases_count, key=self.bases_count.get)

    def __str__(self):
        length = self.len()
        return f"(Length: {length}) {self.strbases}" if length is not None else self.strbases

    def len(self):
        if self.strbases in ["NULL", "ERROR"]:
            return None
        return len(self.strbases)

    def GET(self, service_name):
        return f"GET {self} {service_name}"

# self es una forma de acceder a las variables y métodos de la instancia de la clase desde dentro de la propia clase.
