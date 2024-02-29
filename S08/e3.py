import socket

# SERVER IP, PORT
PORT = 8081
IP = "192.168.1.35"  # depends on the computer the server is running

while True:
    # First, create the socket
    # We will always use these parameters: AF_INET and SOCK_STREAM
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        # establish the connection to the Server (IP, PORT)
        s.connect((IP, PORT))

        # Ask the user to enter a message
        message = input("Enter your message: ")

        # Send data. No strings can be sent, only bytes
        # It's necessary to encode the string into bytes
        s.send(str.encode(message))

        # Receive data from the server
        msg = s.recv(2048)
        print("MESSAGE FROM THE SERVER:\n")
        print(msg.decode("utf-8"))

    except Exception as e:
        print("An error occurred:", e)

    # Closing the socket after receiving the response
    s.close()




