contraseña_correcta="romero123"
usuario_correcto="romerodaniel2098"

intentos=+1

while True:
    usuario=input("ingrese el usuario: ")
    contraseña=input("ingrese la contraseña: ")

    intentos+=1
    
    if usuario == usuario_correcto and contraseña==contraseña_correcta:

        print("Inicio de sesion corecto")
        break 
    else: print("usuario o contraseña invalidos")

    if intentos==3:
        print("Demadiados intentos, bloqueo temporal")
        break   

