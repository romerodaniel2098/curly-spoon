# Adds a new product to the inventory if it doesn't already exist
def add_product(inventory, name, price, quantity):
    # Check if the product is already in the inventory
    if name in inventory:
        print(f"El producto{name} ya existe. Usa la opción de actualizar.")
    else:
        # Add the product as a tuple (price, quantity)
        inventory[name] = (price, quantity)
        print(f"Producto {name} añadido con exito.")

# Displays information for a specific product
def view_product(inventory, name):
    product = inventory.get(name)
    if product:
        price, quantity = product
        print(f"Producto: {name}, Precio: ${price:.2f}, Cantidad: {quantity}")
    else:
        print(f"El producto {name} no se encuentra en el inventario.")

# Updates the price of an existing product
def update_price(inventory, name, new_price):
    if name in inventory:
        _, quantity = inventory[name]
        inventory[name] = (new_price, quantity)
        print(f"El producto {name} actualizado a ${new_price:.2f}.")
    else:
        print(f"No se ṕuede actualizar. El producto {name} no existe.")

# Deletes a product from the inventory
def delete_product(inventory, name):
    if name in inventory:
        del inventory[name]
        print(f"Producto {name} eliminado del inventario.")
    else:
        print(f"No se puede eliminar. El producto {name} no existe.")

# Calculates the total value of the inventory (price * quantity for each product)
def total_inventory_value(inventory):
    total = sum(map(lambda item: item[1][0] * item[1][1], inventory.items()))
    print(f"Valor total del inventario: ${total:.2f}")
    return total

# Requests a float input from the user and validates it
def request_float(message):
    while True:
        entry = input(message)
        try:
            return float(entry)
        except ValueError:
            print("Porfavor ingrese un número valido.")

# Requests an integer input from the user and validates it
def request_int(message):
    while True:
        entry = input(message)
        try:
            return int(entry)
        except ValueError:
            print("Porfavor ingrese un número entero valido.")

# Interactive menu for inventory management
def menu():
    inventory = {}  # Dictionary storing the products
    while True:
        print("\n Menú del Inventario")
        print("1. Añadir un Producto")
        print("2. Consultar un Producto")
        print("3. Actualizar Precio")
        print("4. Eliminar producto")
        print("5. Calcular Valor total del Inventario")
        print("0. Salir")

        option = input("Selecciona una Opción: ")

        if option == "1":
            name = input("Nombre del Producto: ").strip()
            price = request_float("Precio del Producto: ")
            quantity = request_int("Cantidad Disponible: ")
            add_product(inventory, name, price, quantity)

        elif option == "2":
            name = input("Nombre del Producto a Consultar: ").strip()
            view_product(inventory, name)

        elif option == "3":
            name = input("Nombre del producto a Actualizar: ").strip()
            new_price = request_float("Nuevo Precio: ")
            update_price(inventory, name, new_price)

        elif option == "4":
            name = input("Nombre del Producto a Eliminar: ").strip()
            delete_product(inventory, name)

        elif option == "5":
            total_inventory_value(inventory)

        elif option == "0":
            print("Saliendo del Inventario. Adiós!")
            break

        else:
            print("Opción invalida. Intente Nuevamente.")

# Run the program
menu()