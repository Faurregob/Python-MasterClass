peso = float(input("Ingrese por favor su peso en KG: "))
altura = float(input("Ingrese por favor su Altura en Metros: "))

IMC = peso / (altura ** 2)

print(f"\nPeso: {peso}\n"
      f"Altura: {altura}\n"
      f"IMC Calculado: {IMC:.2f}")


if IMC < 18.5:
    print("\nClasificación: Bajo Peso")
elif IMC >= 18.5 and IMC < 24.9:
    print("Clasificación: Peso Normal")
elif IMC >= 25 and IMC < 29.9:
    print("Clasificación: Sobrepeso")
else:
    print("Clasificación: Obesidad")

