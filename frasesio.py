from modules import extract
from modules import Convert


print("|________Bienvenid@s a FrasesIO________|")

frase = input("\nPor favor introduce una frase para expecificarte que tipo es la palabra, recuerda que debes de poner un punto final cuando termines la frase: ").lower()

palabra = Convert(frase).get_palabra()

