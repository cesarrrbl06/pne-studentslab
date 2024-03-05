from seq0 import *
from Client0 import Client


PRACTICE = 2
EXERCISE = 5

print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")

# -- Parameters of the server to talk to
IP1 = "192.168.1.36"  # your IP address
PORT1 = 8080

IP2 = "192.168.1.36"
PORT2 = 8081

# -- Create a client object
c1 = Client(IP1, PORT1)
c2 = Client(IP2, PORT2)

# -- Test the ping method
print(c1)
print(c2)

genes = ["FRAT1"]
for gene in genes:
    seq = seq_read_fasta(f"{gene}.txt")

fragments = [seq[i:i + 10] for i in range(0, len(seq), 10)]
print("Gene FRAT1:" + seq)
for i, fragment in enumerate(fragments[:10]):
    print(f"Fragment {i + 1}: {fragment}")
    if i % 2 == 0:
        response = c1.talk(fragment)
    else:
        response = c2.talk(fragment)

