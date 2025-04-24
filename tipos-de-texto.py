
# empresa de relojes
# en este programa lo que haremos es aplicar descuentos a los productos comprados
# se aplicará un descuento del 10% en base a la compra de 10 relojes

reloj = int(input("Ingresar número de relojes => "))
precio_unitario = int(input("Ingresar precios de reloj unitario => "))

if reloj >= 10:
    descuento = 0.10
else:
    descuento = 0

subtotal = reloj * precio_unitario
total = subtotal - (subtotal * descuento)

print(f"\nSubtotal: ${subtotal}")
print(f"Descuento aplicado: {descuento * 100}%")
print(f"Total a pagar: ${total}")

