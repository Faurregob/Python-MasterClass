edad = int(input("Ingrese su Edad: "))
salario = float(input("Ingrese su salario mensual: "))
prestamo = float(input("Ingrese el monto del préstamo que desea solicitar: "))
pagos = int(input("Ingrese el número de años a Pagar: "))
garantia = input("¿Tiene Garantia? (Si/No): ").lower()
if edad < 18 or edad > 80:
    resultado = "Rechazado: Edad no permitida."
elif salario < 2000000:
    resultado = "Rechazado: Salario insuficiente."
elif prestamo > salario * 12:
    resultado = "Rechazado: Monto del préstamo demasiado alto."
elif pagos < 1 or pagos > 30:
    resultado = "Rechazado: Plazo de pago no permitido."
elif prestamo > 50000000 and garantia != "si":
    resultado = "Rechazado: Garantía requerida para préstamos mayores a 50 millones."
else:
    resultado = "Aprobado."

# Datos del Solicitante
print("\n--- Datos del Solicitante ---")
print(f"Edad: {edad} años")
print(f"Salario mensual: ${salario:,.2f}")
print(f"Monto del préstamo solicitado: ${prestamo:,.2f}")
print(f"Plazo de pago: {pagos} años")
print(f"¿Tiene garantía? {'Sí' if garantia == 'si' else 'No'}")
print(f"Resultado de la solicitud: {resultado}")
