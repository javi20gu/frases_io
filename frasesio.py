from modules import extract


print("|________Bienvenid@s a FrasesIO________|")

frase = input("\nPor favor introduce una frase para expecificarte que tipo es la palabra: ").lower()
palabras = frase.lower().split(" ")

for palabra in palabras:
    print("La palabra |-{}-| es de tipo -> {}".format(palabra, extract(palabra)))