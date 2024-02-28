from Client0 import *
from Seq1 import *
from seq0 import *
from pathlib import Path

PRACTICE = 2
EXERCISE = 4

print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")

# -- Parameters of the server to talk to
IP = "212.128.255.93"  # your IP address
PORT = 8081

# -- Create a client object
c = Client(IP, PORT)

# -- Test the ping method
print(c)

genes = ["U5", "ADA", "FRAT1"]
for gene in genes:
    seq = seq_read_fasta(f"{gene}.txt")

    print(f"Sending the {genes} to the server...")
    response = c.talk(f"{seq}")
    print(f"Response: {response}")
