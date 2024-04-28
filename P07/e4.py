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
gene_dict = {"FRAT1": "ENSG00000165879"}
gene_name = input("Please enter the gene name: ")
gene_id = gene_dict.get(gene_name)
if not gene_id:
    print(f"Gene name {gene_name} not found in the gene dictionary.")
    exit()

ENDPOINT = f"/sequence/id/{gene_id}?content-type=application/json"

URL = SERVER + ENDPOINT

print()
print(f"Server: {SERVER}")
print(f"URL: {URL}")

conn = http.client.HTTPConnection(SERVER)

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
        if json_data.get('version') == 9:
            print("Gene :", gene_name)
            print(f"Description: {json_data.get('desc')}")
            sequence = json_data.get('seq')
            print(info_response(sequence))
            print("PING OK! The database is running!")
        else:
            print("The server is down!")
    else:
        print("No data received from the server.")
else:
    print("Failed to reach the server.")
