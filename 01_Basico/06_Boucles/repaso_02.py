'''
Reto Nivel 2 — for

Después del primero:

Pide una palabra.
Recorre letra por letra.
Cuenta cuántas vocales tiene.
'''

palabra = input("Ingrese una palabra: ")
contador_vocales = 0

for letra in palabra:
    if letra.lower() in 'aeiou':
        contador_vocales += 1

print(f"La palabra '{palabra}' tiene {contador_vocales} vocales.")
