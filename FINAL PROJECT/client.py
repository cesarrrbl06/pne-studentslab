import requests


def print_response(response):
    if response.ok:
        data = response.json()
        for key, value in data.items():
            print(f"{key}: {value}")
    else:
        print(f"Error: {response.status_code}")


def main():
    base_url = "http://localhost:8080"

    while True:
        print("\nChoose an option:")
        print("1. Welcome message")
        print("2. List species")
        print("3. Karyotype info")
        print("4. Chromosome length")
        print("5. Gene sequence")
        print("6. Gene info")
        print("7. Gene sequence calculation")
        print("8. Gene list")
        print("9. Exit")
        choice = input("Enter your choice (1-9): ")

        if choice == '1':
            response = requests.get(base_url, params={'json': '1'})
            print_response(response)
        elif choice == '2':
            limit = input("Enter the limit for species listing: ")
            response = requests.get(f"{base_url}/listSpecies", params={'limit': limit, 'json': '1'})
            print_response(response)
        elif choice == '3':
            species = input("Enter the species name: ")
            response = requests.get(f"{base_url}/karyotype", params={'species': species, 'json': '1'})
            print_response(response)
        elif choice == '4':
            species = input("Enter the species name: ")
            chromosome = input("Enter the chromosome: ")
            response = requests.get(f"{base_url}/chromosome",
                                    params={'species': species, 'chromosome': chromosome, 'json': '1'})
            print_response(response)
        elif choice == '5':
            gene = input("Enter the gene symbol: ")
            response = requests.get(f"{base_url}/geneSeq", params={'gene': gene, 'json': '1'})
            print_response(response)
        elif choice == '6':
            gene = input("Enter the gene symbol: ")
            response = requests.get(f"{base_url}/geneInfo", params={'gene': gene, 'json': '1'})
            print_response(response)
        elif choice == '7':
            gene = input("Enter the gene symbol: ")
            response = requests.get(f"{base_url}/geneCalc", params={'gene': gene, 'json': '1'})
            print_response(response)
        elif choice == '8':
            chromo = input("Enter the chromosome: ")
            start = input("Enter the start position: ")
            end = input("Enter the end position: ")
            response = requests.get(f"{base_url}/geneList",
                                    params={'chromo': chromo, 'start': start, 'end': end, 'json': '1'})
            print_response(response)
        elif choice == '9':
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
