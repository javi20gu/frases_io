from modules import extract, ABREVIACIONES


print("|________Bienvenid@s a FrasesIO________|")

# El usuario introduce toda la frase
frase = input("\nPor favor introduce una frase para expecificarte que tipo es la palabra: ").lower()
# Lo convierte en una lista mediante los espacios
palabras = frase.lower().split(" ")

# Recorre todas las palabras introducidas
for palabra in palabras:
    
    # Si la palabra existe en el diccionario
    if not extract(palabra):
        print("\n\nLa palabra |-{}-| es: ".format(palabra), end='')
        
        # Recorremos cada tipo de la lista con su indice
        for i, tipo in enumerate(extract(palabra)):
            print(ABREVIACIONES[tipo], end="")

            # Comprobamos que la longitud de la lista sea mayor a mas de un elemento 
            if len(extract(palabra)) > 1 and (i+1) < len(extract(palabra)):
                print(" o ", end='')

    # Si la palabra no existe
    else:
        print("\n\nLa palabra |-{}-| aún no está en el diccionario".format(palabra),end='')
        
