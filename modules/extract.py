import requests
from bs4 import BeautifulSoup


def extract(palabra: str):
    # Obtenemos los datos, segun la palabra que introduzcamos.
    r = requests.get("http://www.wordreference.com/definicion/{}".format(palabra))
    # Declaramos una lista para almacenar los posibles tipos.
    tipo = []
    # Verificamos que va a responder con el codigo 200.
    if r.status_code == 200:
        # Extraemos todos los datos
        soup = BeautifulSoup(r.text, "html.parser")
        # Comprobamos que la palabra exista.
        if soup.find("ol", {"class": "entry"}) != None:
            # Buscamos todas las definiciones.
            definiciones = soup.find_all("ol", {"class": "entry"})
            # Vamos una por una, para así añadirlo a la variable tipo.
            for definicion in definiciones:
                indice = definicion.getText().find(".")
                tipo.append(definicion.getText()[:indice])
            # Retornamos los tipos de la palabra.
            return tipo    
        # En caso de que no lo encuentre retorna False.
        else:
            return False
            