from modules import extract, ABREVIACIONES

def frasesio():
    print("|________Bienvenid@s a FrasesIO________|")

    # El usuario introduce toda la frase
    frase = input("\nIntroduce una frase: ").lower()
    # Lo convierte en una lista mediante los espacios
    palabras = frase.lower().split(" ")

    # Recorre todas las palabras introducidas
    for palabra in palabras:
        tipos = extract(palabra)
        # Si la palabra existe en el diccionario
        if tipos != None:
            tipos = map(lambda tipo: ABREVIACIONES[tipo], tipos)
            resultado = " o ".join(tipos)
            print("\n\nLa palabra |-{}-| es de tipo: {}\n"
                  .format(palabra, resultado), end="")
        # Si la palabra no existe
        else:
            print(
                "\n\nLa palabra |-{}-| aún no está"
                " en el diccionario\n".format(palabra), end="")


if __name__ == '__main__':
    frasesio()
