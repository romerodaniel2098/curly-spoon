frase=input("escribe una frase: ")

palabras= frase.split()

contador= {}

for palabra in palabras:
    if palabra in contador:
        contador[palabra] += 1
    else:
        contador[palabra] = 1

for palabra, cantidad in contador.items():
    print(f"{palabra}: {cantidad}")
