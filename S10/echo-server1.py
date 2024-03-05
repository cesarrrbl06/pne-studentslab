import socket
import termcolor

# Configure the Server's IP and PORT
PORT = 8081
IP = "212.128.255.93"  # this IP address is local, so only requests from the same machine are possible

# -- Step 1: create the socket
ls = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# -- Step 2: Bind the socket to server's IP and PORT
ls.bind((IP, PORT))

# -- Step 3: Configure the socket for listening
ls.listen()

print("The server is configured!")

while True:
    (rs, address) = ls.accept()
    print(f"Message received: {address}")# To admit the clients and returns a tuple. Which is the socket and the address
    msg = rs.recv(2048).decode("utf-8")
    termcolor.cprint(("The client says..." + msg), "green")
    mes2 = f"ECHO: {msg}"
    rs.send(mes2.encode())
    rs.close()

# -- Close the socket
ls.close()