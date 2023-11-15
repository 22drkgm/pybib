import requests
import csv
import argparse

def fetch_data_from_doi(doi):
    response = requests.get(f"https://api.crossref.org/works/{doi}")
    if response.status_code == 200:
        return response.json()["message"]
    else:
        print(f"Error fetching data for DOI {doi}")
        return None

def format_authors(authors):
    return ' and '.join([f"{author['given']} {author['family']}" for author in authors])

def generate_bibtex_entry(data):
    authors = data.get('author', [])
    first_author = authors[0] if authors else {}
    last_name = first_author.get('family', 'N/A')
    year = data.get('published-print', {}).get('date-parts', [['N/A']])[0][0]

    return f"@article{{{last_name}{year},\n  title={{ {data.get('title', 'N/A')} }},\n  author={{ {format_authors(authors)} }},\n  journal={{ {data.get('container-title', 'N/A')} }},\n  year={{ {year} }}\n}}"

def save_bibtex_entries(bibtex_entries):
    with open('references.bib', 'w') as file:
        for entry in bibtex_entries:
            file.write(entry + '\n')

def generate_bibtex_entries(dois):
    bibtex_entries = []
    for doi in dois:
        data = fetch_data_from_doi(doi)
        if data:
            bibtex_entry = generate_bibtex_entry(data)
            bibtex_entries.append(bibtex_entry)
    return bibtex_entries

def main():
    parser = argparse.ArgumentParser(description="Generate BibTeX entries from a CSV file.")
    parser.add_argument("--csv", help="Specify the CSV file path.")

    args = parser.parse_args()

    if not args.csv:
        print("Please provide the path to the CSV file.")
        return

    with open(args.csv, 'r') as csv_file:
        dois = [row[0] for row in csv.reader(csv_file)]

    bibtex_entries = generate_bibtex_entries(dois)

    save_bibtex_entries(bibtex_entries)
    print("BibTeX entries have been created. Check 'references.bib'.")

if __name__ == "__main__":
    main()

