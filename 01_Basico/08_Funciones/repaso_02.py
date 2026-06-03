def validar_salario(salario):
    return salario > 0

def crear_empleados(nombre, salario, departamento):
    return {
        'nombre': nombre,
        'salario': salario,
        'departamento': departamento,
    }

def calcular_bono(salario):
    bono = (salario * 10)/100
    return bono

def calcular_salario_final(salario, bono):
    salario_total = salario + bono
    return salario_total

empleado = []

while True:
    print("Menú de opciones:")
    print('1. Registrar Empleado\n'
          '2. Ver todos los empleados\n'
          '3. Calcular bono de un empleado\n'
          '4. Salir')

    opcion = int(input('Seleccione alguna de las Opciones: '))

    if opcion == 1:
        nombre = input('Ingrese el nombre del empleado: ')
        salario = float(input('Ingrese el salario del empleado: '))
        departamento = input('Ingrese el departamento del Empleado: ')
        if validar_salario(salario):
            empleado_nuevo = crear_empleados(nombre, salario, departamento)
            empleado.append(empleado_nuevo)
            print("Empleado registrado exitosamente")
        else:
            print('Salario no válido. Debe ser un número positivo.')
    elif opcion == 2:
        for emp in empleado:
            print(f"Nombre: {emp['nombre']}, Salario: {emp['salario']}, Departamento: {emp['departamento']}")
    elif opcion == 3:
        nombre = input('Ingrese el nombre del empleado para calcular su bono: ')
        encontrado = False
        for emp in empleado:
            if emp['nombre'] == nombre:
                bono = calcular_bono(emp['salario'])
                salario_final = calcular_salario_final(emp['salario'], bono)
                print(f"Empleado: {emp['nombre']}, Salario: {emp['salario']}, Bono: {bono}, Salario Final: {salario_final}")
                encontrado = True
                break
        if not encontrado:
            print('Empleado no encontrado.')
    elif opcion == 4:
        print('Saliendo del programa.')
        break
    else:
        print('Opción no válida. Por favor, ingrese un número del 1 al 4.')




