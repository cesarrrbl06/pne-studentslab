import http.server
import socketserver
from urllib.parse import parse_qs, urlparse
import jinja2 as j
from Seq1 import *
import termcolor

PORT = 8080
socketserver.TCPServer.allow_reuse_address = True


def read_html_file(filename):
    contents = Path("html/" + filename).read_text()
    contents = j.Template(contents)
    return contents


def seq_read_fasta(filename):
    file_contents = Path(filename).read_text()
    list_contents = file_contents.split('\n')
    dna_sequence = ''.join(list_contents[1:])  # Join all lines except the header
    return dna_sequence


def info_response(sequence):
    base_counts = {'A': 0, 'T': 0, 'C': 0, 'G': 0}
    total_bases = len(sequence)
    for base in sequence:
        if base in base_counts:
            base_counts[base] += 1
    percentages = {base: f"{round((count / total_bases) * 100, 2)}%" for base, count in base_counts.items()}
    info = f"Sequence: {sequence}<br>Total length: {total_bases}<br>"
    info += "<br>".join([f"{base}: {count} ({percentages[base]})" for base, count in base_counts.items()])
    return info


sequences = {
    "0": 'ATCGATCGATCGATC',
    "1": 'TACGTACGTACGTAC',
    "2": 'GCTAGCTAGCTAGCT',
    "3": 'CATGCATGCATGCAT',
    "4": 'AGCTAGCTAGCTAGC'
}

genes = ["U5", "ADA", "FRAT1", "FXN", "RNU6_269P"]


class TestHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):
        termcolor.cprint(self.requestline, 'green')
        url_path = urlparse(self.path)
        path = url_path.path
        arguments = parse_qs(url_path.query)

        if path == "/":
            filename = "index.html"
            contents = read_html_file(filename).render(context={})
        elif path == "/ping":
            filename = "ping.html"
            contents = read_html_file(filename).render(context={})
        elif path == "/get":
            filename = "get.html"
            if "n" in arguments:
                n = arguments["n"][-1]
                sequence = sequences.get(n)
                if sequence is not None:
                    contents = read_html_file(filename).render(context={"todisplay": sequence, "sequence_number": n})
                else:
                    filename = "error.html"
                    contents = read_html_file(filename).render(context={})
        elif path == "/gene":
            filename = "gene.html"
            if "name" in arguments:
                name = arguments["name"][-1]
                if name in genes:
                    seq = seq_read_fasta(f"{name}.txt")
                    contents = read_html_file(filename).render(context={"todisplay": seq, "gene_name": name})
                else:
                    filename = "error.html"
                    contents = read_html_file(filename).render(context={})
        elif path == "/operation":
            filename = "operation.html"
            if "msg" and "rev" in arguments:
                msg = arguments["msg"][0]
                seq = Seq(strbases=msg)
                rev = seq.seq_reverse()
                contents = read_html_file(filename).render(context={"todisplay": msg, "result": rev, "operation_name": "Rev"})
            elif "msg" and "comp" in arguments:
                msg = arguments["msg"][0]
                seq = Seq(strbases=msg)
                comp = seq.seq_complement()
                contents = read_html_file(filename).render(context={"todisplay": msg, "result": comp, "operation_name" : "Comp"})
            elif "msg" and "info" in arguments:
                msg = arguments["msg"][0]
                info = info_response(msg)
                contents = read_html_file(filename).render(context={"todisplay": msg, "result": info, "operation_name": "Info"})


        else:
            filename = "error.html"
            contents = read_html_file(filename).render(context={})

        print(arguments)

        self.send_response(200)
        self.send_header('Content-Type', 'html')
        self.send_header('Content-Length', len(contents.encode()))
        self.end_headers()
        self.wfile.write(contents.encode())
        return


Handler = TestHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("Serving at PORT", PORT)
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("")
        print("Stopped by the user")
        httpd.server_close()
