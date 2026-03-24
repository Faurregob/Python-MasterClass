monto_inversion = float(input('Ingrese el monto de la Inversion Inicial: '))
porcentaje = float(input('Ingrese el porcentaje del Retorno Anual: '))
anios = int(input('Ingrese la cantidad de Años: '))

monto_final = monto_inversion * (1 + porcentaje/100) ** anios
ganancia = monto_final - monto_inversion

print(f"Monto Inicial: ${monto_inversion:.0f}\n"
      f"Porcentaje Retorno: {porcentaje:.0f}%\n"
      f"Numero de Años: {anios}\n"
      f"Monto Final: ${monto_final:.0f}\n"
      f"Ganacia Obtenida: ${ganancia:.0f}")
