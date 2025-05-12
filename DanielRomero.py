# Añade un nuevo producto al inventario si no existe ya
def añadir_producto(inventario, nombre, precio, cantidad):
    # Verifica si el producto ya está en el inventario
    if nombre in inventario:
        print(f"El producto {nombre} ya existe. Usa la opción de actualizar.")
    else:
        # Agrega el producto como una tupla (precio, cantidad)
        inventario[nombre] = (precio, cantidad)
        print(f"Producto {nombre} añadido con éxito.")

# Consulta la información de un producto específico
def consultar_producto(inventario, nombre):
    producto = inventario.get(nombre)
    if producto:
        precio, cantidad = producto
        print(f"Producto: {nombre}, Precio: ${precio:.2f}, Cantidad: {cantidad}")
    else:
        print(f"El producto {nombre} no se encuentra en el inventario.")

# Actualiza el precio de un producto si existe
def actualizar_precio(inventario, nombre, nuevo_precio):
    if nombre in inventario:
        _, cantidad = inventario[nombre]
        inventario[nombre] = (nuevo_precio, cantidad)
        print(f"El producto {nombre} actualizado a ${nuevo_precio:.2f}.")
    else:
        print(f"No se puede actualizar. El producto {nombre} no existe.")

# Elimina un producto del inventario si existe
def eliminar_producto(inventario, nombre):
    if nombre in inventario:
        del inventario[nombre]
        print(f"Producto {nombre} eliminado del inventario.")
    else:
        print(f"No se puede eliminar. El producto {nombre} no existe.")

# Calcula el valor total del inventario (precio * cantidad de cada producto)
def valor_total_inventario(inventario):
    total = sum(map(lambda item: item[1][0] * item[1][1], inventario.items()))
    print(f"Valor total del inventario: ${total:.2f}")
    return total

# Solicita un número decimal al usuario y valida la entrada
def solicitar_float(mensaje):
    while True:
        entrada = input(mensaje)
        try:
            return float(entrada)
        except ValueError:
            print("Por favor, ingrese un número válido.")

# Solicita un número entero al usuario y valida la entrada
def solicitar_int(mensaje):
    while True:
        entrada = input(mensaje)
        try:
            return int(entrada)
        except ValueError:
            print("Por favor, ingrese un número entero válido.")

# Menú interactivo para la gestión del inventario
def menu():
    inventario = {}  # Diccionario que almacena los productos
    while True:
        print("\nMenú del Inventario")
        print("1. Añadir un producto")
        print("2. Consultar un producto")
        print("3. Actualizar precio")
        print("4. Eliminar un producto")
        print("5. Calcular valor total del inventario")
        print("0. Salir")

        opción = input("Selecciona una opción: ")

        if opción == "1":
            nombre = input("Nombre del producto: ").strip()
            precio = solicitar_float("Precio del producto: ")
            cantidad = solicitar_int("Cantidad disponible: ")
            añadir_producto(inventario, nombre, precio, cantidad)

        elif opción == "2":
            nombre = input("Nombre del producto a consultar: ").strip()
            consultar_producto(inventario, nombre)

        elif opción == "3":
            nombre = input("Nombre del producto a actualizar: ").strip()
            nuevo_precio = solicitar_float("Nuevo precio: ")
            actualizar_precio(inventario, nombre, nuevo_precio)

        elif opción == "4":
            nombre = input("Nombre del producto a eliminar: ").strip()
            eliminar_producto(inventario, nombre)

        elif opción == "5":
            valor_total_inventario(inventario)

        elif opción == "0":
            print("Saliendo del inventario. ¡Adiós!")
            break

        else:
            print("Opción inválida. Intente nuevamente.")

# Ejecuta el programa
menu()
