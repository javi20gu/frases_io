import requests
from bs4 import BeautifulSoup

URL = "http://www.wordreference.com/definicion/"


def extract(palabra: str):
    # Obtenemos los datos, segun la palabra que introduzcamos.
    r = requests.get(URL + palabra)
    # Declaramos una lista para almacenar los posibles tipos.
    tipos = []
    # Verificamos que va a responder con el codigo 200.
    if r.status_code == 200:
        # Extraemos todos los datos
        soup = BeautifulSoup(r.text, "html.parser")
        # Buscamos todas las definiciones.
        definiciones = soup.find_all("ol", {"class": "entry"})

        # Comprobamos que la palabra exista.
        if definiciones:
            # Vamos una por una, para así añadirlo a la variable tipo.
            for definicion in definiciones:
                indice = definicion.getText().find(".")
                tipos.append(definicion.getText()[:indice])

            # Retornamos los tipos de la palabra.
            return tipos
        # En caso de que no lo encuentre
        return None
