from modules import extract, ABREVIACIONES


def frasesio():
    print("|________Bienvenid@s a FrasesIO________|")

    # El usuario introduce toda la frase
    palabras = input("\nIntroduce una frase: ").lower().split(" ")

    # Recorre todas las palabras introducidas
    for palabra in palabras:
        tipos = extract(palabra)
        # Si la palabra existe en el diccionario
        if tipos:
            try:
                tipos = [ABREVIACIONES[tipo] for tipo in tipos]
                resultado = " o ".join(tipos)
                print("\n\nLa palabra |-{}-| es de tipo: {}\n"
                    .format(palabra, resultado), end="")
            except KeyError as a:
                print("Error ({}): Abreviatura no incluida en el diccionario ({}), si quiere informar utilize el email -> javierhidalgo_c@hotmail.com".format(palabra, a))
        # Si la palabra no existe
        else:
            print(
                "\n\nLa palabra |-{}-| aún no está"
                " en el diccionario\n".format(palabra), end="")


if __name__ == '__main__':
    frasesio()
