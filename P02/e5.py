from seq0 import *
from Client0 import Client
from Seq1 import *

PRACTICE = 2
EXERCISE = 5

print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")

# -- Parameters of the server to talk to
IP = "192.168.1.35"  # your IP address
PORT = 8081

# -- Create a client object
c = Client(IP, PORT)

# -- Test the ping method
print(c)

genes = ["FRAT1"]
for gene in genes:
    seq = seq_read_fasta(f"{gene}.txt")


fragments = [seq[i:i+10] for i in range(0, len(seq), 10)]
print("Gene FRAT1:" + seq)
for i, fragment in enumerate(fragments[:5]):
    print(f"Fragment {i+1}: {fragment}")
    response = c.talk(fragment)









