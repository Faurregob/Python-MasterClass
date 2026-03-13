edad_cliente = int(input("Señor Cliente, Ingrese por favor su edad: "))
dinero = float(input("Ingrese el monto que posee en este momento: $ "))
producto = input("Ingrese el nombre del producto a comprar: ")
valor_product = 250.55


if edad_cliente < 18:
    print("No tienes la edad suficiente para comprar en la tienda.")
elif dinero < valor_product:
    print("No te alcanza para comprar el producto:\n"
          f"Te hace falta: $ {valor_product - dinero}")
else:
    print("Felicidades, Haz realizado tu compra exitosamente")


