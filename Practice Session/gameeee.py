import socket
import random

class NumberGuesser:
    def __init__(self):
        self.IP = "127.0.0.1"
        self.PORT = 8082
        self.MAX_OPEN_REQUESTS = 5
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.number_attempts = 0
        self.secret_number = random.randint(1, 100)
        self.attempts = []

    def guess(self, client_number):
        self.attempts.append(client_number)
        if client_number == self.secret_number:
            return "You won after {} attempts".format(len(self.attempts))
        elif client_number < self.secret_number:
            return "Higher"
        else:
            return "Lower"

    def launch_game(self):
        try:
            self.server_socket.bind((self.IP, self.PORT))
            self.server_socket.listen(self.MAX_OPEN_REQUESTS)

            while True:
                print("Game server running and waiting for connections at {}, {}".format(self.IP, self.PORT))
                (client_socket, address) = self.server_socket.accept()

                self.number_attempts += 1
                print("ATTEMPT: {}. From the IP: {}".format(self.number_attempts, address))

                msg = client_socket.recv(2048).decode("utf-8")
                print("Message from player {}".format(msg))

                response = self.guess(int(msg))
                client_socket.send(response.encode())
                client_socket.close()

        except socket.error:
            print("Problems using ip {} port {}. Is the IP correct? Do you have port permission?".format(self.IP, self.PORT))

        except KeyboardInterrupt:
            print("Game stopped by the user")
            self.server_socket.close()



server = NumberGuesser()
server.launch_game()

