

# aća le pediremos al usuario que coloque el nombre del producto
producto=input("ingrese el nombre del producto: ")        
 
#luego le pedimos al usuario que coloque el precio del producto
precio=int(input("ingrese el precio del producto: "))

#aća pondremos el precio del producto, si el usuario coloca un numero menor a 0 el sistema arrojara error, si nomostrara la cantidad
if precio <= 0: 
    print("el precio del producto no es valido")
else:
    quantity = int(input("ingresa la cantidad: "))

#acá pondremos la cantidad del producto, si el usuario pone 0 la cantidad no sera valida
if quantity <= 0:
    print("la cantidad del producto no es valido") 
else:
    descuento = int(input("ingrese el descuento: ")) 

#acá pondremos el descuento, el cual ira de 0 a 100, si no esta en esos parametros, el descuento no se aplicara
if descuento < 0 or descuento >=100:
    print("el descuento no cumple los parametros")
else: 
    resultado = precio * quantity 
    
    desctotal = resultado * (descuento / 100)

    #acá ya integraremos lo que es el producto, con su precio, la cantidad y su respectivo descuento
print ("el nombre de tu producto es: ", producto, "precio del producto es", precio, "la cantidad del producto es" ,quantity, "el descuento es: ",descuento)

print ("el  monto total de la compra es: " ,(resultado) - (desctotal))
