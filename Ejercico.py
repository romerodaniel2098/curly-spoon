def solicitar_datos_estudiante():
    nombre= input("ingresa nombre del estudiamte")
    notas=[]
    for i in range(1, 4):
        while True:
            try:
                nota = float(input(f"ingrese la nota{i}(0 a 5):"))
                if 0 <= nota <= 5:
                    notas.append(nota) 
                    break
                else:
                    print("La nota debe estar entre 0 y 5.")
            except ValueError:
                print("Porfavor ingrese un número valido")
    return nombre, notas

def calcular_promedio(notas):
    return sum(notas)/len(notas)

def mostrar_resultado(nombre, promedio):
    estado= "APROBO" if promedio >= 3.0 else "REPROBO"
    print(f"\n{nombre} tiene un promedio de {promedio:.2f} y {estado}.\n")
           

def main():
    print("==calculadora de promedios de estudiantes==")
    while True:
        try:
            cantidad=int(input("¿Cuantos estudiantes desea ingresar?"))
            if cantidad >0:
               break
            else: 
                print("ingrese un número mayor a 0.")
        except ValueError:
          print("porfavor ingrese un múmero entero valido.")

    for _ in range(cantidad):
          nombre, notas = solicitar_datos_estudiante()
          promedio = calcular_promedio(notas)
          mostrar_resultado(nombre, promedio)

# Ejecutar el programa
if __name__ == "__main__":
    main()