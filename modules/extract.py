import requests
from bs4 import BeautifulSoup


def extract(palabra: str):
    r = requests.get("http://www.wordreference.com/definicion/{}".format(palabra))

    if r.status_code == 200:
        soup = BeautifulSoup(r.text, "html.parser")
        definicion = soup.find("ol", {"class": "entry"}).getText()
        tipo = []
        palabras = ""
        for letra in definicion:
            if letra == ".":
                tipo.append(palabras)
                palabras = ""
            else:
                palabras += letra

        return tipo[0]
