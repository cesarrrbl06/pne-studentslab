from Client0 import *

PORT = 8081
IP = "212.128.255.101"

c = Client(IP, PORT)
for i in range(5):
    msg = "Message" + str(i)
    response = c.talk(msg)

    print(f"To server: {msg}")
    print(f"From server: {response}")