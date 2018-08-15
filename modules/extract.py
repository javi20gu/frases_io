import requests
from bs4 import BeautifulSoup


URL = "http://www.wordreference.com/definicion/"
RESPUESTAS = {
    "m": "Nombre Masculino",
    "f": "Nombre Femenino",
    "v": "Verbo",
    "tr": "Verbo",
    "suf": "Sufijo",
    "interj": "interjección",
    "art": "Articulo",
    "intr": "Verbo",
    "adj": "Adjetivo",
    "conj": "Conjunción",
    "pron": "Pronombre",
    "contr": "Contracción de la preposición + artículo",
    "adv": "Adverbio",
}


def extract(palabra: str):
    request = requests.get(URL + palabra)

    if request.status_code == 200:
        soup = BeautifulSoup(request.text, "html.parser")
        definition = soup.find("ol", {"class": "entry"})

        if definition:
            tipo = definition.getText().split(". ")[0]
            return RESPUESTAS.get(tipo, f"Tipo no asignado: {tipo}")

    return "No encontrada"
