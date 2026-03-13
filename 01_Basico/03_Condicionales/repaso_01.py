numero = int(input("Usuario, por favor ingrese un numero: "))
mensaje1 = "positivo" if numero > 0 else ("negativo" if numero < 0 else "cero")
mensaje2 = "numero par" if numero % 2 == 0 else "numero impar"

print(f"El usuario ingreso el numero ({numero})\n"
      f"Es un numero: {mensaje1.capitalize()}\n"
      f"El numero es: {mensaje2.capitalize()}")
