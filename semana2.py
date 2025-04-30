def ingresar_calificaciones():
    # Solicitar al usuario ingresar varias calificaciones
    calificaciones = []
    while True:
        try:
            calificacion = float(input("Ingresa una calificación (0-10) o escribe 'fin' para terminar: "))
            if 0 <= calificacion <= 10:
                calificaciones.append(calificacion)
            else:
                print("La calificación debe estar entre 0 y 10. Intenta de nuevo.")
        except ValueError:
            print("Para terminar, escribe 'fin'.")
            break
    return calificaciones

def calcular_promedio(calificaciones):
    # Calcular el promedio de las calificaciones
    if len(calificaciones) == 0:
        return 0
    suma = sum(calificaciones)
    return suma / len(calificaciones)

def contar_calificaciones_mayores(calificaciones, valor):
    # Contar cuántas calificaciones son mayores que el valor dado
    contador = 0
    for cal in calificaciones:
        if cal > valor:
            contador += 1
    return contador

def verificar_calificacion_especifica(calificaciones, calificacion_buscar):
    # Contar cuántas veces aparece una calificación específica
    contador = 0
    for cal in calificaciones:
        if cal == calificacion_buscar:
            contador += 1
    return contador

def main():
    print("¡Bienvenido al programa de calificaciones!")
    
    # Paso 1: Ingresar calificaciones
    calificaciones = ingresar_calificaciones()
    
    # Paso 2: Solicitar el valor para comparar
    valor_comparar = float(input("Ingresa un valor para comparar con las calificaciones: "))
    
    # Paso 3: Calcular el promedio
    promedio = calcular_promedio(calificaciones)
    print(f"\nEl promedio de las calificaciones es: {promedio:.2f}")
    
    # Paso 4: Contar calificaciones mayores que el valor dado
    conteo_mayores = contar_calificaciones_mayores(calificaciones, valor_comparar)
    print(f"\nNúmero de calificaciones mayores que {valor_comparar}: {conteo_mayores}")
    
    # Paso 5: Solicitar una calificación específica para buscar
    calificacion_especifica = float(input("Ingresa una calificación específica para contar cuántas veces aparece: "))
    conteo_especifico = verificar_calificacion_especifica(calificaciones, calificacion_especifica)
    print(f"\nLa calificación {calificacion_especifica} aparece {conteo_especifico} veces.")
    
    # Paso 6: Verificación de aprobación
    for cal in calificaciones:
        if cal >= 6:
            print(f"La calificación {cal} es aprobatoria.")
        else:
            print(f"La calificación {cal} no es aprobatoria.")

# Ejecutar el programa
if __name__ == "__main__":
    main()

    