
from seq0 import *
from Client0 import *
from Seq1 import *

PRACTICE = 2
EXERCISE = 5

print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")

# -- Parameters of the server to talk to
IP = "127.0.0.1"  # your IP address
PORT = 8080

# -- Create a client object
c = Client(IP, PORT)

# -- Test the ping method
print(c)