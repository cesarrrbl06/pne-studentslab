from Seq1 import *


genes = ["U5", "ADA", "FRAT1", "FXN", "RNU6_269P"]
for gene in genes:
    seq = Seq(f"{gene}.txt")
    if seq.strbases != "NULL":
        most_frequent = seq.most_frequent_base()  # Call the method on seq object
        print(f"Gene {gene}: Most frequent base: {most_frequent}")





