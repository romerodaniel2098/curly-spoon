inventario = {}



    if opcion == "1":
        nombre = input("Nombre del producto: ").strip()
        precio = float(input("Precio del producto: "))
        cantidad = int(input("Cantidad disponible: "))
        if nombre in inventario:
            print(f"El producto '{nombre}' ya existe. Usa la opción de actualizar.")
        else:
            inventario[nombre] = (precio, cantidad)
            print(f"Producto '{nombre}' añadido con éxito.")

    elif opcion == "2":
        nombre = input("Nombre del producto a consultar: ").strip()
        if nombre in inventario:
            precio, cantidad = inventario[nombre]
            print(f"Producto: {nombre} | Precio: ${precio:.2f} | Cantidad: {cantidad}")
        else:
            print(f"El producto '{nombre}' no se encuentra en el inventario.")

    elif opcion == "3":
        nombre = input("Nombre del producto a actualizar: ").strip()
        if nombre in inventario:
            nuevo_precio = float(input("Nuevo precio: "))
            precio, cantidad = inventario[nombre]
            inventario[nombre] = (nuevo_precio, cantidad)
            print(f"Precio del producto '{nombre}' actualizado a ${nuevo_precio:.2f}.")
        else:
            print(f"No se puede actualizar. El producto '{nombre}' no existe.")

    elif opcion == "4":
        nombre = input("Nombre del producto a eliminar: ").strip()
        if nombre in inventario:
            del inventario[nombre]
            print(f"Producto '{nombre}' eliminado del inventario.")
        else:
            print(f"No se puede eliminar. El producto '{nombre}' no existe.")

    elif opcion == "5":
        total = sum(precio * cantidad for precio, cantidad in inventario.values())
        print(f"Valor total del inventario: ${total:.2f}")

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