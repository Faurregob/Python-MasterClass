compra = float(input("Ingrese el valor de la compra: "))
porcentaje = 15 if compra >= 500000 else 5
valor_descuento = (compra * porcentaje)/100
print(f"Valor de la Compra: ${compra}\n"
      f"Porcentaje Descuento: {porcentaje}%\n"
      f"Valor Descuento: ${valor_descuento}\n"
      f"Valor Total= {compra - valor_descuento}")