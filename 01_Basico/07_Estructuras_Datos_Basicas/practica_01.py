persona = {
    "nombre": "Juan",
    "edad": 25,
    "ciudad": "Madrid"
}

calificaciones = {
    "Matemática": 8.5,
    "Inglés": 9.0,
    "Historia": 7.5
}

print(persona['nombre'])
print(persona['edad'])
print(persona['ciudad'])

persona['profesion'] = 'Ingeniero'
print(persona['profesion'])

print("Llaves: " + ", ".join(persona.keys()))
print("Valores: " + ", ".join(str(v) for v in persona.values()))
