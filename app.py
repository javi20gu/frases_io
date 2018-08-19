from sys import argv

from frasesio import frasesio
from web import app


def main():
    if "server" in argv or "-s" in argv:
        app.run()
    elif "help" in argv or "-h" in argv:
        print("Comandos Utililes:\
        \nserver o -s: Inicia la app en la web.\
        \nhelp o -h: Te dice los comandos utiles.\
        \nconsole o -c: Inicia en la consola.\
        ")
    elif "console" in argv or "-c" in argv:
        frasesio()
    else:
        print(
            "Error: Comando incorrecto,"
            " consulte el comando help o -h.")


if __name__ == '__main__':
    main()
