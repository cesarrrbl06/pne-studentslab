import socket
from pathlib import Path

IP = "127.0.0.1"
PORT = 8080


def process_client(s):
    req_raw = s.recv(2000)
    req = req_raw.decode()
    lines = req.split('\n')
    req_line = lines[0]

    if req_line.startswith("GET /info/A"):
        file_content = Path("./html/info/A.html").read_text()
        body = file_content
    elif req_line.startswith("GET /info/C"):
        file_content = Path("./html/info/C.html").read_text()
        body = file_content
    elif req_line.startswith("GET /info/G"):
        file_content = Path("./html/info/G.html").read_text()
        body = file_content
    elif req_line.startswith("GET /info/T"):
        file_content = Path("./html/info/T.html").read_text()
        body = file_content
    else:
        body = ""

    status_line = "HTTP/1.1 200 OK\n"
    header = "Content-Type: text/html\n"
    header += f"Content-Length: {len(body)}\n"
    response_msg = status_line + header + "\n" + body
    cs.send(response_msg.encode())


ls = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ls.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
ls.bind((IP, PORT))
ls.listen()

print("Server bases!")

while True:
    print("Waiting for clients....")
    try:
        (cs, client_ip_port) = ls.accept()
    except KeyboardInterrupt:
        print("Server stopped!")
        ls.close()
        exit()
    else:
        process_client(cs)
        cs.close()