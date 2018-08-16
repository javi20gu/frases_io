import requests
from bs4 import BeautifulSoup
from .dicc import ABREVIACIONES


def extract(palabra: str):
    r = requests.get("http://www.wordreference.com/definicion/{}".format(palabra))

    if r.status_code == 200:
        soup = BeautifulSoup(r.text, "html.parser")
        if soup.find("ol", {"class": "entry"}) !=  None:
            definicion = soup.find("ol", {"class": "entry"}).getText()
            tipo = []
            palabras = ""
            for letra in definicion:
                if letra == ".":
                    tipo.append(palabras)
                    palabras = ""
                else:
                    palabras += letra
            if tipo[0] != "":
                return ABREVIACIONES[tipo[0]]
            else:
                return "Tipo no asignado: {}".format(tipo[0])
        else:
            print("\nError: Palabra no encontrada en el diccionaria, intentelo con otra")
            return "No encontrada"
