# cantidad_notas = int(input("Ingrese la cantidad de notas: "))
# contador = 0
# for i in range(cantidad_notas):
#     nota = float(input(f"Ingrese la nota N° {i+1}: "))
#     contador += nota
#
# calificacion = contador / cantidad_notas

calificacion = float(input(f"Ingrese la nota entre (0-10): "))

if calificacion < 0.0 or calificacion > 10.0:
    print("Debes ingresar una calificacion entre (0-10).")
elif calificacion >= 9.0 and calificacion <= 10.0:
    print(f"Nota: {calificacion} / Calificación: 'Excelente'")
elif calificacion >= 8.0 and calificacion <= 8.9:
    print(f"Nota: {calificacion} / Calificación: 'Muy Bien'")
elif calificacion >= 7.0 and calificacion <= 7.9:
    print(f"Nota: {calificacion} / Calificación: 'Bien'")
elif calificacion >= 6.0 and calificacion <= 6.9:
    print(f"Nota: {calificacion} / Calificación: 'Aceptable'")
else:
    print(f"Nota: {calificacion} / Calificación: 'Reprobado'")
