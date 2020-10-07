from bs4 import BeautifulSoup
import requests


def get_ontologies(ont_code, verbose = False):

    page = requests.get(f"https://www.uniprot.org/uniprot/{ont_code}")
    soup = BeautifulSoup(page.content, "html.parser")

    # Get all biological process data
    BPs = soup.find_all(class_="noNumbering biological_process")
    # Get ontologies names
    ontologies = BPs[0].find_all("a")
    # Separate names in a list
    names = [str(name.get_text()) for name in ontologies]

    if verbose:
        print("\n".join(names))

    return names

with open("DBPR.txt", "r") as f:
    data = f.read()

get_ontologies(data, verbose=True)