def solicitar_datos():
    nombre=input("ingresa nombre del estudiante")
    notas=[]
    for i in range(1, 5):
        while True:
            try:
                nota=float(input(f"ingrese la nota{i}(0 a 5):"))
                if 0 <= nota <= 5:
                    notas.append(nota)
                    break
                else:
                    print("la nota debe estar entre 0 y 5.")
            except ValueError:
                print("porfavor ingrese un numero valido")
    while True:
        try:
            asistencia=float(input(f"ingrese el porcentaje de asistencia (0 a 100)"))
            if 0 <= asistencia <=100:
                break
            else:
                print("la asistencia debe estar entre 0 y 100.")    
        except ValueError:
            print("porfavor ingrese un número valido.")
    return nombre, notas, asistencia

def calcular_promedio(notas):
    return sum(notas)/len(notas)

def mostrar_resultados(nombre, promedio, asistencia):
    if promedio >=3.0 and asistencia >=80:
        estado="APROBO"
    else:
        estado="REPROBO"
        print(f"\n{nombre} tiene un promedio de {promedio:.2f}, una asistencia de {asistencia:.0f}%, y {estado}.\n")

def main():
    nombre, notas, asistencia = solicitar_datos()
    promedio = calcular_promedio(notas)
    mostrar_resultados(nombre, promedio, asistencia)

if __name__ == "__main__":
    main()               

                  
