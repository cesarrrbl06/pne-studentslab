import http.client
import json

SERVER = "rest.ensembl.org"
ENDPOINT = "/sequence/id/ENSG00000207552?content-type=application/json"

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
        if json_data.get('version') == 1:
            print("Gene : MIR633")
            print(f"Description: {json_data.get('desc')}")
            print(f"Bases: {json_data.get('seq')}")

            print("PING OK! The database is running!")
        else:
            print("The server is down!")
    else:
        print("No data received from the server.")
else:
    print("Failed to reach the server.")
