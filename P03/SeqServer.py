import socket
import termcolor
from P01.e8 import MySeq


class SeqServer:
    def __init__(self):
        self.PORT = 8080
        self.IP = "127.0.0.1"
        self.MAX_OPEN_REQUESTS = 5
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sequences = ["ATCGTACGATCGATCG", "CGATACGATGCTAGCT", "TCGATCGATCGTAGCT", "GCTAGCTAGCATCGAT",
                          "ATCGATCGTAGCTAGC"]

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

                message = self.return_response(str(msg))
                send_bytes = str.encode(message)
                client_socket.send(send_bytes)
                client_socket.close()

        except socket.error:
            print("Problems using ip {} port {}. Is the IP correct? Do you have port permission?".format(self.IP,
                                                                                                         self.PORT))

        except KeyboardInterrupt:
            print("Server stopped by the user")
            self.server_socket.close()

    def ping_response(self):
        print("Print command!")
        return "OK"

    def get_response(self, index):
        if 0 <= index < len(self.sequences):
            sequence = self.sequences[index]
            print("Sequence returned: {}".format(sequence))  # Print sequence to server terminal
            return sequence
        else:
            return "Invalid index. Please provide a number between 0 and 4."

    def info_response(self, sequence):
        base_counts = {'A': 0, 'T': 0, 'C': 0, 'G': 0}
        total_bases = len(sequence)
        for base in sequence:
            if base in base_counts:
                base_counts[base] += 1
        percentages = {base: f"{round((count / total_bases) * 100, 2)}%" for base, count in base_counts.items()}
        print("Total length:", len(sequence))
        print("Base Counts:", base_counts)
        print("Base percentages:", percentages)
        return base_counts, percentages, total_bases

    def complementary(self, sequences):
        if self.sequences in ["NULL", "ERROR"]:
            return self.sequences
        else:
            complement_dict = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
            return ''.join([complement_dict[base] for base in self.sequences])



    def return_response(self, msg):
        if msg.startswith("PING"):
            print("PING")
            return self.ping_response(), None, None, None
        elif msg.startswith("GET"):
            termcolor.cprint("GET", "green")
            index = int(msg.split()[1])  # Extract the index from the message
            return self.get_response(index), None, None, None
        elif msg.startswith("INFO"):
            termcolor.cprint("INFO", "green")
            sequence = msg.split()[1]
            base_counts, percentages, length = self.info_response(sequence)
            percentages_str = "Base percentages: None" if percentages is None else "\n".join(
                [f"{base}: {percentage}%" for base, percentage in percentages.items()])
            return f"Total length: {length}\nBase Counts: {base_counts}\n{percentages_str}"


server = SeqServer()
server.start_server()
