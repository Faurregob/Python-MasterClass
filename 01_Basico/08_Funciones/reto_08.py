def calcular_promedio(calificaciones):
    suma = sum(calificaciones)
    promedio = suma / len(calificaciones)
    return promedio

def obtener_maxima(calificaciones):
    return max(calificaciones)

def obtener_minima(calificaciones):
    return min(calificaciones)

def clasificar_promedio(promedio):
    if promedio >= 9.0:
        return "Excelente"
    elif promedio >= 8.0:
        return "Muy Bien"
    elif promedio >= 7.0:
        return "Bien"
    elif promedio >= 6.0:
        return "Aceptable"
    else:
        return "Reprobado"

calificaciones = []
for i in range(5):
    nota = float(input(f"Ingrese la calificación del estudiante {i+1}: "))
    calificaciones.append(nota)

promedio = calcular_promedio(calificaciones)
maxima = obtener_maxima(calificaciones)
minima = obtener_minima(calificaciones)
clasificacion = clasificar_promedio(promedio)

print(f"Promedio: {promedio:.2f}")
print(f"Calificación máxima: {maxima}")
print(f"Calificación mínima: {minima}")
print(f"Clasificación del promedio: {clasificacion}")



