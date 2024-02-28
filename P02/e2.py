
from Client0 import *

PRACTICE = 2
EXERCISE = 2

print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")

# -- Parameters of the server to talk to
IP = "212.128.255.93" # your IP address
PORT = 8081

# -- Create a client object
c = Client(IP, PORT)

# -- Test the ping method
print(c)