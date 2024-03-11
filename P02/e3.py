from Client0 import *

PRACTICE = 2
EXERCISE = 2

print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")

# -- Parameters of the server to talk to
IP = "127.0.0.1" # your IP address
PORT = 8081

# -- Create a client object
c = Client(IP, PORT)

# -- Test the ping method
print(c)


print("Sending a message to the server...")
response = c.talk("GET")
print(f"Response: {response}")

