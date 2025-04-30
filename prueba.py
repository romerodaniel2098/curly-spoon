clave_correcta="oro123"

intentos=0

while True: 
    clave_usuario = input("introduce la contraseña para abrir la caja fuerte: ")

    intentos+= 1
    
    if clave_usuario==clave_correcta:
        print("¡caja abierta! bien hecho")
        break
    else:
        print("contraseña incorrecta")

if intentos==3:
    print("Demasiado intentos. Caja bloqueada.")
    

        
