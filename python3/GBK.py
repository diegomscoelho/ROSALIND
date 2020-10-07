from bs4 import BeautifulSoup
import requests


def get_number_publications(genus, from_date, to_date, verbose = False):

    url = f"https://www.ncbi.nlm.nih.gov/nuccore?term=%28%22{genus}%22%5BOrganism%5D%20AND%20%28%22{from_date}"
    url += f"%22%5BPDAT%5D%20%3A%20%22{to_date}%22%5BPDAT%5D%29&cmd=DetailsSearch"
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")

    # Get result count(
    query = soup.find_all(class_="result_count")[0].get_text()
    number = query.split()[-1]
    
    if verbose:
        print(f"Number of publication is: {number}")

    return number

with open("GBK.txt", "r") as f:
    genus, from_date, to_date = f.read().split()

get_number_publications(genus, from_date, to_date, verbose=True)