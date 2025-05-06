def añadir_producto(inventario, nombre, precio, cantidad):
    if nombre in inventario:
        print(f"El producto '{nombre}' ya existe. Usa la opción de actualizar.")
    else:
        inventario[nombre] = (precio, cantidad)
        print(f"Producto '{nombre}' añadido con éxito.")

def consultar_producto(inventario, nombre):
    producto = inventario.get(nombre)
    if producto:
        precio, cantidad = producto
        print(f"Producto: {nombre} | Precio: ${precio:.2f} | Cantidad: {cantidad}")
    else:
        print(f"El producto '{nombre}' no se encuentra en el inventario.")

def actualizar_precio(inventario, nombre, nuevo_precio):
    if nombre in inventario:
        _, cantidad = inventario[nombre]
        inventario[nombre] = (nuevo_precio, cantidad)
        print(f"Precio del producto '{nombre}' actualizado a ${nuevo_precio:.2f}.")
    else:
        print(f"No se puede actualizar. El producto '{nombre}' no existe.")

def eliminar_producto(inventario, nombre):
    if nombre in inventario:
        del inventario[nombre]
        print(f"Producto '{nombre}' eliminado del inventario.")
    else:
        print(f"No se puede eliminar. El producto '{nombre}' no existe.")

def valor_total_inventario(inventario):
    total = sum(map(lambda item: item[1][0] * item[1][1], inventario.items()))
    print(f"Valor total del inventario: ${total:.2f}")
    return total

def solicitar_float(mensaje):
    while True:
        entrada = input(mensaje)
        try:
            return float(entrada)
        except ValueError:
            print("Por favor, ingresa un número válido.")

def solicitar_int(mensaje):
    while True:
        entrada = input(mensaje)
        try:
            return int(entrada)
        except ValueError:
            print("Por favor, ingresa un número entero válido.")

def menu():
    inventario = {}
    while True:
        print("\n--- Menú de Gestión de Inventario ---")
        print("1. Añadir producto")
        print("2. Consultar producto")
        print("3. Actualizar precio")
        print("4. Eliminar producto")
        print("5. Calcular valor total del inventario")
        print("6. Mostrar todos los productos")
        print("0. Salir")
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            nombre = input("Nombre del producto: ").strip()
            precio = solicitar_float("Precio del producto: ")
            cantidad = solicitar_int("Cantidad disponible: ")
            añadir_producto(inventario, nombre, precio, cantidad)

        elif opcion == "2":
            nombre = input("Nombre del producto a consultar: ").strip()
            consultar_producto(inventario, nombre)

        elif opcion == "3":
            nombre = input("Nombre del producto a actualizar: ").strip()
            nuevo_precio = solicitar_float("Nuevo precio: ")
            actualizar_precio(inventario, nombre, nuevo_precio)

        elif opcion == "4":
            nombre = input("Nombre del producto a eliminar: ").strip()
            eliminar_producto(inventario, nombre)

        elif opcion == "5":
            valor_total_inventario(inventario)

        elif opcion == "6":
            if inventario:
                print("\nInventario actual:")
                for nombre, (precio, cantidad) in inventario.items():
                    print(f"{nombre}: Precio ${precio:.2f}, Cantidad {cantidad}")
            else:
                print("El inventario está vacío.")

        elif opcion == "0":
            print("Saliendo del programa. ¡Hasta luego!")
            break

        else:
            print("Opción inválida. Intenta nuevamente.")

# Ejecutar el programa
menu()
