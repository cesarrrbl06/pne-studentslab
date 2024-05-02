import http.server
import socketserver
from urllib.parse import parse_qs, urlparse
import jinja2 as j
from Seq1 import *
import termcolor
import requests

PORT = 8080
socketserver.TCPServer.allow_reuse_address = True


def read_html_file(filename):
    contents = Path("html/" + filename).read_text()
    contents = j.Template(contents)
    return contents


def list_species(limit=None):
    response = requests.get("http://rest.ensembl.org/info/species", headers={"Content-Type": "application/json"})
    if response.ok:
        data = response.json()
        species = [specie['name'] for specie in data['species']]
        if limit:
            species = species[:int(limit)]
        return species
    else:
        print("Error connecting to the Ensembl database")


class TestHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):
        termcolor.cprint(self.requestline, 'green')
        url_path = urlparse(self.path)
        path = url_path.path
        arguments = parse_qs(url_path.query)

        if path == "/":
            filename = "FPe1 web.html"
            contents = read_html_file(filename).render(context={})
        elif path == "/listSpecies":
            filename = "species.html"
            if "limit" in arguments:
                limit = arguments["limit"][-1]
                species = list_species(limit)
            else:
                species = list_species()
            contents = read_html_file(filename).render(context={"species": species})  # Added closing parenthesis here



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

