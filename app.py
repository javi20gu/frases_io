import sys

from frasesio import frasesio
from web import app


def main():
    if "server" in sys.argv:
        app.run()
    else:
        frasesio()


if __name__ == '__main__':
    main()
