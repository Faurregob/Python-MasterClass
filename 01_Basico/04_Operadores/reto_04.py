
# Variables a Ingresar
salario = float(input("Ingrese su salario Mensual: "))
gastos_ali = float(input("Ingrese el valor de sus Gastos Alimentarios: "))
gastos_trans = float(input("Ingrese el valor de sus Gastos en Transportes: "))
gastos_ent = float(input("Ingrese el valor de sus Gastos en Entrenamientos: "))
gastos_ser = float(input("Ingrese el valor de sus Gastos de Servicios Publicos: "))

# Acumulador de todos los gastos
total_gastos = 0
total_gastos += gastos_ali
total_gastos += gastos_trans
total_gastos += gastos_ent
total_gastos += gastos_ser

# Salario restante
restante = salario - total_gastos

# Porcentaje Gastos/Salario
porcentaje = (total_gastos / salario * 100)
# Porcentaje Disponible
porcentaje_disp = (100 - porcentaje)

# Imprimir
print(f"Salario: ${salario:.2f}\n"
      "Desgloce de todos los Gastos\n"
      f" - Gastos Alimentacion: ${gastos_ali:.2f}\n"
      f" - Gastos Transportes: ${gastos_trans:.2f}\n"
      f" - Gastos Entrenamiento: ${gastos_ent:.2f}\n"
      f" - Gastos Servicios Publicos ${gastos_ser:.2f}\n"
      f"Total Gastos: {total_gastos:.0f}\n"
      f"Dinero Restante: {restante:.0f}\n"
      f"Porcentaje Gastos: {porcentaje:.2f}%\n"
      f"Porcentaje Disponible: {porcentaje_disp:.2f}%")






