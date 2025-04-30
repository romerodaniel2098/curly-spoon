

def adivina_el_numero():
    # El número secreto es un número aleatorio entre 1 y 100
    numero_secreto = (7)
    intento = None
    
    print("¡Bienvenido al juego de Adivina el número!")
    print("Estoy pensando en un número entre 1 y 100. ¡Intenta adivinarlo!")

    while intento != numero_secreto:
        
        intento = int(input("¿Cuál es tu intento? "))
        
        if intento < numero_secreto:
            print("Demasiado bajo. Intenta de nuevo.")
        elif intento > numero_secreto:
            print("Demasiado alto. Intenta de nuevo.")
        else:
            print(f"¡Felicidades! Has adivinado el número {numero_secreto}.")


adivina_el_numero()
