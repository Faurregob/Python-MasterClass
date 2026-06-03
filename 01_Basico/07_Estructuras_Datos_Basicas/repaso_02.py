calificaciones = {
    'Juan': 8.5,
    'María': 9.0,
    'Pedro': 7.5,
}

while True:
    print("Menú de opciones:")
    print("1. Ver todas las calificaciones\n"
          "2. Buscar calificacion de un estudiante\n"
          "3. Añadir un estudiante\n"
          "4. Actualizar calificacion de un estudiante\n"
          "5. Eliminar un estudiante\n"
          "6. Salir")

    opcion = int(input("Ingrese el número de la opción deseada: "))

    if opcion == 1:
        for estudiante, calificacion in calificaciones.items():
            print(f"{estudiante}: {calificacion}")
    elif opcion == 2:
        estudiante = input("Ingrese el nombre del estudiante: ")
        if estudiante in calificaciones:
            print(f"{estudiante}: {calificaciones[estudiante]}")
        else:
            print("Estudiante no encontrado.")
    elif opcion == 3:
        estudiante = input("Ingrese el nombre del nuevo estudiante: ")
        if estudiante not in calificaciones:
            calificacion = float(input("Ingrese la calificación: "))
            if calificacion >= 0 and calificacion <= 10:
                calificaciones[estudiante] = calificacion
            else:
                print("Calificación debe estar entre 0 y 10")
        else:
            print("El estudiante ya existe.")
    elif opcion == 4:
        estudiante = input("Ingrese el nombre del estudiante: ")
        if estudiante in calificaciones:
            nueva_calificacion = float(input("Ingrese la nueva calificación: "))
            if nueva_calificacion >= 0 and nueva_calificacion <= 10:  # ✅ Agregar
                calificaciones[estudiante] = nueva_calificacion
            else:
                print("Calificación debe estar entre 0 y 10")
        else:
            print("Estudiante no encontrado.")
    elif opcion == 5:
        estudiante = input("Ingrese el nombre del estudiante: ")
        if estudiante in calificaciones:
            del calificaciones[estudiante]
        else:
            print("Estudiante no encontrado.")
    elif opcion == 6:
        print("Saliendo del programa.")
        break
    else:
        print("Opción no válida. Por favor, ingrese un número del 1 al 6.")







