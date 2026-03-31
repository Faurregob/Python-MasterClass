calificacion = float(input("Ingrese la calificación del examen: "))
asistencia = float(input("Ingrese el porcentaje de asistencia: "))
comportamiento = input("Ingrese el comportamiento del estudiante (Excelente, Bueno, Regular, Malo): ").lower()
trabajos = int(input("Ingrese el número de trabajos entregados: "))

if calificacion < 6.0:
    resultado = "Reprobado por calificación."
elif asistencia < 75.0:
    resultado = "Reprobado por asistencia."
elif comportamiento == "malo":
    resultado = "Reprobado por comportamiento."
elif trabajos < 3:
    resultado = "Reprobado por trabajos no entregados."
else:
    resultado = "Aprobado."

# Datos del Estudiante
print("\n--- Datos del Estudiante ---")
print(f"Calificación del examen: {calificacion}")
print(f"Porcentaje de asistencia: {asistencia}%")
print(f"Comportamiento: {comportamiento.capitalize()}")
print(f"Número de trabajos entregados: {trabajos}")
print(f"Resultado final: {resultado}")