import socket


class SeqServer:
    def __init__(self):
        self.PORT = 8081
        self.IP = "127.0.0.1"
        self.MAX_OPEN_REQUESTS = 5
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def start_server(self):
        try:
            self.server_socket.bind((self.IP, self.PORT))
            self.server_socket.listen(self.MAX_OPEN_REQUESTS)

            while True:
                print("Waiting for connections at {}, {} ".format(self.IP, self.PORT))
                (client_socket, address) = self.server_socket.accept()

                print("CONNECTION: From the IP: {}".format(address))

                msg = client_socket.recv(2048).decode("utf-8")
                print("Message from client: {}".format(msg))

                message = "Hello from the Cesar server\n"
                send_bytes = str.encode(message)
                client_socket.send(send_bytes)
                client_socket.close()

        except socket.error:
            print("Problems using ip {} port {}. Is the IP correct? Do you have port permission?".format(self.IP,
                                                                                                         self.PORT))

        except KeyboardInterrupt:
            print("Server stopped by the user")
            self.server_socket.close()


server = SeqServer()
server.start_server()
