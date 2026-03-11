edad = int(input("Ingrese su edad: "))
estudiante = input("¿Eres Estudiante Si/No?: ")
estudiante = estudiante.lower()
valor_compra = float(input("Ingrese el valor de la compra: $"))





if edad >= 65:
    descuento = (valor_compra * 20) / 100

elif estudiante == "si" :
    descuento = (valor_compra * 15) / 100

elif valor_compra >= 500000:
    descuento = (valor_compra * 10) / 100

else:
    descuento = (valor_compra * 0) / 100

total_compra = (valor_compra - descuento)
print("-----CLIENTE----\n"
      f"Estudiante: {estudiante.capitalize()}\n"
      f"Edad: {edad}\n"
      f"Valor Compra: ${valor_compra:.0f}\n"
      f"Ahorro: -${descuento:.0f}\n"
      f"Total Compra: ${total_compra:.0f}\n"
      "=======================================")



