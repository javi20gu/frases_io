

class Convert:

    def __init__(self, frase: str):
        self.__frase = frase
        self.__palabra = []

    def get_palabra(self):
        palabra = ""
        for letra in self.__frase:

            if letra == " " or letra == ".":
                self.__palabra.append(palabra)
                palabra = ""
            else:
                palabra += letra

        return self.__palabra
