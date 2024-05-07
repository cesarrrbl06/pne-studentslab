import http.server
import socketserver
from urllib.parse import parse_qs, urlparse
import jinja2 as j
import termcolor
import requests
from pathlib import Path

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
        species = [specie['display_name'] for specie in data['species']]
        total_species = len(species)
        if limit:
            species = species[:int(limit)]
        return total_species, species
    else:
        print("Error connecting to the Ensembl database")


def karyotype_info(species):
    response = requests.get(f"http://rest.ensembl.org/info/assembly/{species}",
                            headers={"Content-Type": "application/json"})
    if response.ok:
        data = response.json()
        return data['karyotype']
    else:
        print("Error connecting to the Ensembl database")


def chrom_length(species, region):
    response = requests.get(f"http://rest.ensembl.org/info/assembly/{species}/{region}",
                            headers={"Content-Type": "application/json"})
    if response.ok:
        data = response.json()
        return data['length']
    else:
        print("Error connecting to the Ensembl database")


def gene_find(display_name):
    response = requests.get(f"https://rest.ensembl.org/lookup/symbol/human/{display_name}",
                            headers={"Content-Type": "application/json"})
    if response.ok:
        data = response.json()
        return data["id"]
    else:
        print("Error connecting to the Ensembl database")
        return None



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
                total_species, species = list_species(limit)
            else:
                limit = None
                total_species, species = list_species()
            contents = read_html_file(filename).render(
                context={"total_species": total_species, "species": species, "limit": limit})
        elif path == "/karyotype":
            filename = "karyotype.html"
            if "species" in arguments:
                species = arguments["species"][-1]
                karyotype = karyotype_info(species)
            else:
                species = None
                karyotype = []
            contents = read_html_file(filename).render(
                context={"species": species, "karyotype": karyotype})
        elif path == "/chromosome":
            filename = "chromosomelen.html"
            if "species" in arguments and "chromosome" in arguments:
                species = arguments["species"][-1]
                chromosome = arguments["chromosome"][-1]
                length = chrom_length(species, chromosome)
            else:
                species = None
                chromosome = None
                length = None
            contents = read_html_file(filename).render(
                context={"species": species, "chromosome": chromosome, "length": length})
        elif path == "/geneSeq":
            filename = "geneSeq.html"
            if "gene" in arguments:
                gene_symbol = arguments["gene"][0]
                id = gene_find(gene_symbol)
                if id:
                    response = requests.get(f"https://rest.ensembl.org/sequence/id/{id}",
                                            headers={"Content-Type": "application/json"})
                    if response.ok:
                        data = response.json()
                        seq = data["seq"]
                    else:
                        print("Error connecting to the Ensembl database")
                        seq = None
                else:
                    print(f"No gene found for symbol: {gene_symbol}")
                    seq = None
            else:
                id = None
                seq = None
            contents = read_html_file(filename).render(context={"id": id, "seq": seq})
        elif path == "/geneInfo":
            filename = "geneInfo.html"
            if "gene" in arguments:
                gene_symbol = arguments["gene"][0]
                id = gene_find(gene_symbol)
                if id:
                    response = requests.get(f"https://rest.ensembl.org/sequence/id/{id}",
                                            headers={"Content-Type": "application/json"})
                    if response.ok:
                        data = response.json()
                        seq = data["seq"]
                    else:
                        print("Error connecting to the Ensembl database")
                        seq = None
                else:
                    print(f"No gene found for symbol: {gene_symbol}")
                    seq = None
            else:
                id = None
                seq = None
            contents = read_html_file(filename).render(context={"id": id, "seq": seq})

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
