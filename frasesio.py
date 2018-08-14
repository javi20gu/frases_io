from modules import extract


def main():
    print("|________Bienvenid@s a FrasesIO________|")

    frase = input(
        "Por favor introduce una frase para expecificar de "
        "que tipo es la palabra:\n").lower()
    palabras = frase.lower().split(" ")

    for palabra in palabras:
        print("La palabra |-{}-| es de tipo -> {}".format(palabra, extract(palabra)))


if __name__ == "__main__":
    main()
