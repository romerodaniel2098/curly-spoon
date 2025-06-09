
contraseña_correcta = "micontraseña123"

max_intentos = 10
intentos = 0

def bienvenida():
    print("¡Bienvenido! Acceso concedido.")

while intentos < max_intentos:
    contraseña_usuario = input(f"Intento {intentos + 1}/{max_intentos} - Ingresa la contraseña: ")

    if contraseña_usuario == contraseña_correcta:
        bienvenida() 
        break  
    else:
        print("Contraseña incorrecta. Intente nuevamente.")
        intentos += 1

if intentos == max_intentos:
    print("Has superado el número máximo de intentos. Acceso bloqueado temporalmente.")

                    