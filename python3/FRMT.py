from bs4 import BeautifulSoup
import requests


def get_fasta(entryIDs, verbose = False):

    data = []

    for entryID in entryIDs:

        page = requests.get(f"https://www.ncbi.nlm.nih.gov/nuccore/{entryID}")
        soup = BeautifulSoup(page.content, "html.parser")

        # Get all biological process data
        ID = [id.get_text().split("|")[1] for id in soup.find_all(class_="brieflinkpopdesc") if id.get_text().startswith("gi")][0]
        
        page = requests.get(f"https://www.ncbi.nlm.nih.gov/sviewer/viewer.fcgi?id={ID}&db=nuccore&report=fasta&retmode=text&withmarkup=on&tool=portal&log$=seqview&maxdownloadsize=1000000")
        fasta = str(BeautifulSoup(page.content, "html.parser")).split("\n")

        # Header
        fasta[0] = fasta[0].replace("&gt;", ">")
        fasta = [line for line in fasta if line != ""]

        size = sum([len(read) for read in fasta[1:]])

        if data and size < data[1]:
            data = [fasta, size]
        elif not data:
            data = [fasta, size]

    print("\n".join(data[0]))

    return None

with open("FRMT.txt", "r") as f:
    data = f.read().split()

get_fasta(data, verbose=True)