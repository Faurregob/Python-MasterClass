def suma(a,b):
    return a + b

def resta(a,b):
    return a - b

def multiplicacion(a,b):
    return a * b

def division(a,b):
    if b != 0:
        return a / b
    else:
        return None

def potencia(base,exponente):
    return base ** exponente

while True:
    print("Menú de opciones:")
    print("1. Suma\n"
          "2. Resta\n"
          "3. Multiplicación\n"
          "4. División\n"
          "5. Potencia\n"
          "6. Salir")

    opcion = int(input('Seleccione alguna de las Opciones: '))

    if opcion == 1:
        num1 = float(input('Ingrese el primer número: '))
        num2 = float(input('Ingrese el segundo número: '))
        print(f'El resultado de la suma es: {suma(num1,num2)}')
    elif opcion == 2:
        num1 = float(input('Ingrese el primer número: '))
        num2 = float(input('Ingrese el segundo número: '))
        print(f'El resultado de la resta es: {resta(num1,num2)}')
    elif opcion == 3:
        num1 = float(input('Ingrese el primer número: '))
        num2 = float(input('Ingrese el segundo número: '))
        print(f'El resultado de la multiplicación es: {multiplicacion(num1,num2)}')
    elif opcion == 4:
        num1 = float(input('Ingrese el primer número: '))
        num2 = float(input('Ingrese el segundo número: '))
        resultado = division(num1,num2)
        if resultado is None:
            print('Error: División por cero')
        else:
            print(f'El resultado de la división es: {resultado}')
    elif opcion == 5:
        base = float(input('Ingrese la base: '))
        exponente = float(input('Ingrese el exponente: '))
        print(f'El resultado de la potencia es: {potencia(base,exponente)}')
    elif opcion == 6:
        print('Saliendo del programa.')
        break
    else:
        print('Opción no válida. Por favor, ingrese un número del 1 al 6.')
