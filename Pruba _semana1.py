def añadir_producto(inventario, nombre, precio, cantidad):
    if nombre in inventario:
        print(f"El producto{nombre} ya existe. Usa la opción de actualizar. ")
    else:
        inventario [nombre]= (precio, cantidad)
    print(f"producto {nombre} añadido con exito.")

def consultar_producto(inventario, nombre):
    producto=inventario.get(nombre)
    if producto:
        precio, cantidad= producto
        print(f"Producto:{nombre}, precio:${precio:.2f}, Cantidad: {cantidad}")
    else:
        print("El producto {nombre} no se encuentra en el inventario. ")

def actualizar_precio(inventario, nombre, nuevo_precio):
    if nombre in inventario:
        cantidad=inventario[nombre]  
        inventario[nombre]=(nuevo_precio, cantidad)
        print(f"El producto{nombre} actualizado a ${nuevo_precio:.2f}. ")
    else:
        print(f"No se puede actualizar. El producto {nombre} no existe.")

def eliminar_producto(inventario, nombre):
    if nombre in inventario:
        del inventario[nombre]
        print(f"producto {nombre} eliminado del inventario. ")
    else:
        print(f"No se puede eliminar. El producto {nombre} no existe. ")

def valor_total_inventario(inventario):
    total=sum(map(lambda item:item[1][0]*item [1][1],inventario.items()))
    print(f"Valor total de inventario:${total:.2f}")
    return total

def solicitar_float(mensaje):
    while True:
        entrada=input(mensaje)
        try:
            return float(entrada)
        except ValueError:
            print("Porfavor ingresar un número valido. ")

def solicitar_int(mensaje):
    while True:
        entrada=input(mensaje)
        try:
            return int(entrada)
        except ValueError:
            print("Porfavor ingresa un número entero valido. ")

def menu():
    inventario={}
    while True:
        print("\n Menú del Inventario")
        print("1. Añadir un producto")
        print("2. Consultar un producto")
        print("3. Actualizar Precio ")
        print("4. Eliminar un producto ")
        print("5. Calcular valor total del Inventario ")
        print("0. Salir ")
        opción=input("Serlecciona una opción: ")

        if opción == "1":
            nombre= input("Nombre del Producto: ").strip()
            precio= solicitar_float("Precio del producto: ")
            cantidad= solicitar_int("Cantidad Disponible: ")
            añadir_producto(inventario, nombre, precio, cantidad)
        
        elif opción =="2":
            nombre=input("nombre del producto a consultar: ").strip()
            consultar_producto(inventario, nombre)

        elif opción =="3":
            nombre=input("Nombre del producto a actualizar: ").strip()
            nuevo_precio=solicitar_float("Nuevo precio: ")
            actualizar_precio(inventario, nombre, nuevo_precio)
        
        elif opción =="4":
            nombre=input("Nombre del poducto a eliminar: ").strip()
            eliminar_producto(inventario,nombre)

        elif opción =="5":
            valor_total_inventario(inventario)

        elif opción =="0":
            print("Saliendo del Inventario. ¡Adiós!. ")
            break
        else:
            print("Opción invalida. Intente Nuevamente. ")

menu()
