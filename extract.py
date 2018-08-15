import requests
from bs4 import BeautifulSoup


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
            if tipo[0] == "m":
                return "Nombre Masculino"
            elif tipo[0] == "f":
                return "Nombre Femenino"
            elif tipo[0] == "v":
                return "Verbo"
            elif tipo[0] == "tr":
                return "Verbo"
            elif tipo[0] == "suf":
                return "Sufijo"
            elif tipo[0] == "interj":
                return "interjección"
            elif tipo[0] == "art":
                return "Articulo"
            elif tipo[0] == "intr":
                return "Verbo"
            elif tipo[0] == "adj":
                return "Adjetivo"
            elif tipo[0] == "conj":
                return "Conjunción"
            elif tipo[0] == "pron":
                return "Pronombre"
            elif tipo[0] == "contr":
                return "Contracción de la preposición + artículo"
            elif tipo[0] == "adv":
                return "Adverbio"
            else:
                return "Tipo no asignado: {}".format(tipo[0])
        else:
            print("\nError: Palabra no encontrada en el diccionaria, intentelo con otra")
            return "No encontrada"
