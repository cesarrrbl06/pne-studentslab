import http.client
import json

def info_response(sequence):
    base_counts = {'A': 0, 'T': 0, 'C': 0, 'G': 0}
    total_bases = len(sequence)
    for base in sequence:
        if base in base_counts:
            base_counts[base] += 1
    percentages = {base: f"{round((count / total_bases) * 100, 2)}%" for base, count in base_counts.items()}
    info = f"Sequence: {sequence}\nTotal length: {total_bases}\n"
    info += "\n".join([f"{base}: {count} ({percentages[base]})" for base, count in base_counts.items()])
    return info

SERVER = "rest.ensembl.org"
gene_dict = {
    "FRAT1": {"id": "ENSG00000165879", "version": 9},
    "ADA": {"id": "ENSG00000196839", "version": 14},
    "FXN": {"id": "ENSG00000165060", "version": 15},
    "RNU6_269P": {'id': 'ENSG00000212379', "version": 1},
    "MIR633": {'id': 'ENSG00000207552', "version": 1},
    "TTTY4C": {'id': 'ENSG00000228296', "version": 1},
    "RBMY2YP": {"id": "ENSG00000227633", "version": 1},
    "FGFR3": {"id": "ENSG00000068078", "version": 20 },
    "KDR": {"id": "ENSG00000128052", "version": 10},
    "ANK2": {"id": "ENSG00000145362", "version": 21}
}

conn = http.client.HTTPConnection(SERVER)

for gene_name, gene_info in gene_dict.items():
    gene_id = gene_info["id"]
    gene_version = gene_info["version"]
    ENDPOINT = f"/sequence/id/{gene_id}?content-type=application/json"
    try:
        conn.request("GET", ENDPOINT)
    except ConnectionRefusedError:
        print("ERROR! Cannot connect to the Server")
        exit()

    response = conn.getresponse()

    if response.status == 200:
        data = response.read().decode("utf-8")
        if data:  # Check if data is not empty
            json_data = json.loads(data)
            if json_data.get('version') == gene_version:
                print("Gene :", gene_name)
                print(f"Description: {json_data.get('desc')}")
                sequence = json_data.get('seq')
                print(info_response(sequence))
                print("PING OK! The database is running!")
            else:
                print(f"The server version for {gene_name} does not match the expected version!")
        else:
            print("No data received from the server.")
    else:
        print("Failed to reach the server.")

