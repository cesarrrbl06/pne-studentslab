import http.server
import socketserver
from urllib.parse import parse_qs, urlparse
import jinja2 as j
import termcolor
import requests
from pathlib import Path
import json

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
        species = [(specie['display_name']) for specie in data['species']]
        total_species = len(species)
        if limit:
            species = species[:int(limit)]
        return total_species, species
    else:
        print("Error connecting to the Ensembl database")


def get_scientific_name(common_name):
    response = requests.get("http://rest.ensembl.org/info/species", headers={"Content-Type": "application/json"})
    if response.ok:
        data = response.json()
        for species in data['species']:
            if species['display_name'].lower() == common_name.lower():
                return species['name']
    print("Error connecting to the Ensembl database")
    return None


def handle_plus_in_species_name(species):
    return species.replace(" ", "+")


def karyotype_info(species_name):
    common_name = species_name.replace("+", " ")
    species = get_scientific_name(common_name)
    if species is None:
        print(f"Species {common_name} not found in Ensembl.")
        return None
    species = species.replace(" ", "+")  # replace spaces with '+' in the species name
    response = requests.get(f"http://rest.ensembl.org/info/assembly/{species}",
                            headers={"Content-Type": "application/json"})
    if response.ok:
        data = response.json()
        return data['karyotype']
    else:
        print("Error connecting to the Ensembl database")
        return None



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


def gene_info(display_name):
    response = requests.get(f"https://rest.ensembl.org/lookup/symbol/human/{display_name}",
                            headers={"Content-Type": "application/json"})
    if response.ok:
        data = response.json()
        return data["id", "start", "end", "length", "assembly_name"]
    else:
        print("Error connecting to the Ensembl database")
        return None


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


class TestHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):
        termcolor.cprint(self.requestline, 'green')
        url_path = urlparse(self.path)
        path = url_path.path
        arguments = parse_qs(url_path.query)
        json_requested = 'json' in arguments and arguments['json'][-1] == '1'

        if path == "/":
            if json_requested:
                self.respond_json({"message": "Welcome to the Ensembl API server!"})
            else:
                filename = "FPe1 web.html"
                contents = read_html_file(filename).render(context={})
                self.respond_html(contents)
        elif path == "/listSpecies":
            if "limit" in arguments:
                limit = arguments["limit"][-1]
                if not limit.isdigit() or int(limit) < 1 or int(limit) > 324:
                    print("Limit not valid. It should be a number between 1 and 324.")
                    filename = "error.html"
                    contents = read_html_file(filename).render(context={})
                    self.respond_html(contents)
                    return
                total_species, species = list_species(limit)
            else:
                limit = None
                total_species, species = list_species()
            if json_requested:
                self.respond_json({"total_species": total_species, "species": species})
            else:
                filename = "species.html"
                contents = read_html_file(filename).render(
                    context={"total_species": total_species, "species": species, "limit": limit})
                self.respond_html(contents)
        elif path == "/karyotype":
            if "species" in arguments:
                species = arguments["species"][-1]
                karyotype = karyotype_info(species)
                if not karyotype:
                    error_message = f"Species {species} not found in Ensembl."
                    filename = "error.html"
                    contents = read_html_file(filename).render(context={"error": error_message})
                    self.respond_html(contents)
                    return
            if json_requested:
                self.respond_json({"species": species, "karyotype": karyotype})
            else:
                filename = "karyotype.html"
                contents = read_html_file(filename).render(
                    context={"species": species, "karyotype": karyotype})
                self.respond_html(contents)
        elif path == "/chromosome":
            if "species" in arguments and "chromosome" in arguments:
                species = arguments["species"][-1]
                chromosome = arguments["chromosome"][-1]
                length = chrom_length(species, chromosome)
                if length is None:  # If the species or chromosome does not exist in Ensembl
                    error_message = f"Species {species} or chromosome {chromosome} not found in Ensembl."
                    filename = "error.html"
                    contents = read_html_file(filename).render(context={"error": error_message})
                    self.respond_html(contents)
                    return
            else:
                species = None
                chromosome = None
                length = None
            if json_requested:
                self.respond_json({"species": species, "chromosome": chromosome, "length": length})
            else:
                filename = "chromosomelen.html"
                contents = read_html_file(filename).render(
                    context={"species": species, "chromosome": chromosome, "length": length})
                self.respond_html(contents)



        elif path == "/geneSeq":
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
                    filename = "error.html"
                    contents = read_html_file(filename).render(context={})
                    self.respond_html(contents)
            else:
                id = None
                seq = None
            if json_requested:
                self.respond_json({"id": id, "seq": seq})
            else:
                filename = "geneSeq.html"
                contents = read_html_file(filename).render(context={"id": id, "seq": seq})
                self.respond_html(contents)
        elif path == "/geneInfo":
            if "gene" in arguments:
                gene_symbol = arguments["gene"][0]
                response = requests.get(f"https://rest.ensembl.org/lookup/symbol/human/{gene_symbol}",
                                        headers={"Content-Type": "application/json"})
                if response.ok:
                    data = response.json()
                    id = data.get("id")
                    start = data.get("start")
                    end = data.get("end")
                    length = end - start + 1 if start and end else None
                    assembly_name = data.get("assembly_name")
                else:
                    print(f"No gene found for symbol: {gene_symbol}")
                    filename = "error.html"
                    contents = read_html_file(filename).render(context={})
                    self.respond_html(contents)
            else:
                id = start = end = length = assembly_name = None
            if json_requested:
                self.respond_json(
                    {"id": id, "start": start, "end": end, "length": length, "assembly_name": assembly_name})
            else:
                filename = "geneInfo.html"
                contents = read_html_file(filename).render(
                    context={"id": id, "start": start, "end": end, "length": length, "assembly_name": assembly_name})
                self.respond_html(contents)
        elif path == "/geneCalc":
            if "gene" in arguments:
                gene_symbol = arguments["gene"][0]
                response = requests.get(f"https://rest.ensembl.org/lookup/symbol/human/{gene_symbol}",
                                        headers={"Content-Type": "application/json"})
                if response.ok:
                    data = response.json()
                    id = data.get("id")
                    response_seq = requests.get(f"https://rest.ensembl.org/sequence/id/{id}",
                                                headers={"Content-Type": "application/json"})
                    if response_seq.ok:
                        data_seq = response_seq.json()
                        seq = data_seq["seq"]
                        info = info_response(seq)  # Assign the result to 'info'
                    else:
                        print("Error connecting to the Ensembl database")
                        seq = None
                        info = None
                else:
                    print(f"No gene found for symbol: {gene_symbol}")
                    filename = "error.html"
                    contents = read_html_file(filename).render(context={})
                    self.respond_html(contents)
            else:
                id = None
                seq = None
                info = None
            if json_requested:
                self.respond_json({"id": id, "info": info})
            else:
                filename = "geneCalc.html"
                contents = read_html_file(filename).render(
                    context={"id": id, "info": info})
                self.respond_html(contents)
        elif path == "/geneList":
            if "chromo" in arguments and "start" in arguments and "end" in arguments:
                chromo = arguments["chromo"][0]
                start = arguments["start"][0]
                end = arguments["end"][0]

                # Add a list of valid chromosomes
                valid_chromosomes = [str(i) for i in range(1, 23)] + ['X', 'Y', 'MT']

                # Check if the entered chromosome is valid
                if chromo not in valid_chromosomes:
                    print(f"Invalid chromosome: {chromo}. Please enter a valid chromosome.")
                    filename = "error.html"
                    contents = read_html_file(filename).render(context={})
                    self.respond_html(contents)
                    return  # Make sure to return after responding

                response = requests.get(
                    f"https://rest.ensembl.org/overlap/region/human/{chromo}:{start}-{end}?feature=gene",
                    headers={"Content-Type": "application/json"})
                if response.ok:
                    data = response.json()
                    gene_names = [result['external_name'] for result in data if 'external_name' in result]
                    gene_names_str = ", ".join(gene_names)
                else:
                    print("Error connecting to the Ensembl database")
                    gene_names_str = None
            else:
                chromo = None
                print(f"No chromosome found for: {chromo}")
                filename = "error.html"
                contents = read_html_file(filename).render(context={})
                self.respond_html(contents)
                return
            if json_requested:
                self.respond_json({"chromo": chromo, "start": start, "end": end, "gene_names": gene_names_str})
            else:
                filename = "geneList.html"
                contents = read_html_file(filename).render(
                    context={"chromo": chromo, "start": start, "end": end, "gene_names": gene_names_str})
                self.respond_html(contents)

    def respond_html(self, contents):
        self.send_response(200)
        self.send_header('Content-Type', 'text/html')
        self.send_header('Content-Length', len(contents.encode()))
        self.end_headers()
        self.wfile.write(contents.encode())

    def respond_json(self, data):
        self.send_response(200)
        self.send_header('Content-Type', 'application/json')
        json_data = json.dumps(data)
        self.send_header('Content-Length', len(json_data))
        self.end_headers()
        self.wfile.write(json_data.encode())


Handler = TestHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("Serving at PORT", PORT)
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("")
        print("Stopped by the user")
        httpd.server_close()
