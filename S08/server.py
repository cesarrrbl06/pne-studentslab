import socket

# Configure the Server's IP and PORT
PORT = 8081
IP = "192.168.1.35" # it depends on the machine the server is running
MAX_OPEN_REQUESTS = 5

# Counting the number of connections
number_con = 0

# create an INET, STREAMing socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    s.bind((IP, PORT))
    # become a server socket
    # MAX_OPEN_REQUESTS connect requests before refusing outside connections
    s.listen(MAX_OPEN_REQUESTS)

    while True:
        # accept connections from outside
        print("Waiting for connections at {}, {} ".format(IP, PORT))
        (client_socket, address) = s.accept()

        # Another connection!e
        number_con += 1

        # Print the connection number
        print("CONNECTION: {}. From the IP: {}".format(number_con, address))

        # Read the message from the client, if any
        msg = client_socket.recv(2048).decode("utf-8")
        print("Message from client: {}".format(msg))

        # Send the message
        message = "Hello from the Cesar server\n"
        send_bytes = str.encode(message)
        # We must write bytes, not a string
        client_socket.send(send_bytes)
        client_socket.close()

except socket.error:
    print("Problems using ip {} port {}. Is the IP correct? Do you have port permission?".format(IP, PORT))

except KeyboardInterrupt:
    print("Server stopped by the user")
    s.close()
