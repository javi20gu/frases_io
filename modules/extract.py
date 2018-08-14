import requests
from bs4 import BeautifulSoup


URL = "http://www.wordreference.com/definicion/"


def extract(palabra: str):
    request = requests.get(URL + palabra)

    if request.status_code == 200:
        soup = BeautifulSoup(request.text, "html.parser")
        definition = soup.find("ol", {"class": "entry"}).getText()
        tipo = definition.split(". ")[0]
        return tipo

    return "Not found"
