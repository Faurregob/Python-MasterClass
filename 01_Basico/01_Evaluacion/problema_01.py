# Sistema de Gestion de Presupuesto
salario = float(input("Ingrese su salario mensual: "))
alimentacion = float(input("Ingrese sus gastos de alimentación: "))
vivienda = float(input("Ingrese sus gastos de vivienda: "))
entretenimiento = float(input("Ingrese sus gastos de entretenimiento: "))
ahorros = float(input("Ingrese sus gastos de ahorros: "))

if salario < 1000000:
    exit("Salario muy bajo")



# Total de gastos (usar +=)
total_gastos = 0
total_gastos += alimentacion
total_gastos += vivienda
total_gastos += entretenimiento
total_gastos += ahorros

# Dinero restante (salario - gastos)
dinero_restante = salario - total_gastos

# Porcentaje de gastos
porcentaje_gastos = (total_gastos / salario) * 100

# Porcentaje disponible
porcentaje_disponible = 100 - porcentaje_gastos

# Clasificar la situación financiera
mensaje1 = ("Presupuesto Critico" if porcentaje_gastos > 90 else
           "Presupuesto Ajustado" if porcentaje_gastos > 70 else
           "Presupuesto Normal" if porcentaje_gastos > 50 else
           "Presupuesto Saludable")

# Validar
if total_gastos > salario:
    exit("Gastos superiores al salario")

# Imprimir
print(f"\nSalario mensual: ${salario:,.0f}")
print("\nGestos Mensuales")
print(f"- Gastos de alimentación: ${alimentacion:,.0f}")
print(f"- Gastos de vivienda: ${vivienda:,.0f}")
print(f"- Gastos de entretenimiento: ${entretenimiento:,.0f}")
print(f"- Gastos de ahorros: ${ahorros:,.0f}")
print(f"\nTotal de gastos: ${total_gastos:,.0f}")
print(f"Dinero restante: ${dinero_restante:,.0f}")
print(f"Porcentaje de gastos: {porcentaje_gastos:.2f}%")
print(f"Porcentaje disponible: {porcentaje_disponible:.2f}%")
print(f"\nSituación financiera: {mensaje1}")






