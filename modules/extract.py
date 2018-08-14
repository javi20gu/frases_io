import requests
from bs4 import BeautifulSoup

urls = "http://dle.rae.es/hola"


def extract(palabra: str):
    r = requests.get(urls)
    if r.status_code == 200:
        soup = BeautifulSoup(r, "html.parser")
        name_box = soup.find("abbr", attrs={"class": "d"})
        name = name_box.text.strip()

extract("hola")
