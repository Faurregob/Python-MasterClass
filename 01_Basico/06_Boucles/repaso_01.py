'''
Nivel 1 — while

Crea un programa que:

Pida un número al usuario.
Continúe pidiendo números.
Termine únicamente cuando el usuario escriba el número cero.
Al final debe mostrar:
cuántos números ingresó,
y la suma total.
'''

contador = 0
suma = 0

while True:
    numero = int(input("Ingrese un número (0 para terminar): "))
    if numero == 0:
        break

    contador += 1
    suma += numero

print(f"\nCantidad de números ingresados: {contador}")
print(f"Suma total: {suma}")


