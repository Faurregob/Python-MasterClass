edad = int(input("Señor Usuario, por favor ingrese su edad: "))
salario = float(input("Señor Usuario, por favor ingrese su salario actual: "))

mensaje1 = "Mayor de Edad. " if edad>=18 else "Menor de Edad."
mensaje2 = "Bajo" if salario < 2000000 else "Adecuado"

print(f"El usuario tiene {edad} años y es {mensaje1}")
print(f"El usuario tiene un salario de ${salario:.0f} y es {mensaje2}")
