'''
Crea un programa que simule un cajero automático:
Pide:
Saldo inicial de la cuenta
Menú repetido (while True):
Opción 1: Ver saldo
Opción 2: Depositar dinero
Opción 3: Retirar dinero
Opción 4: Salir
Lógica:
Ver saldo: Imprime el saldo actual
Depositar: Pide cantidad, suma al saldo, imprime nuevo saldo
Retirar: Pide cantidad, valida que haya dinero suficiente, resta del saldo, imprime nuevo saldo
Salir: Usa break para terminar el programa
Validaciones:
No permitir retirar más de lo que hay
No permitir depósitos/retiros negativos
Requisito: Usa while True con break, validaciones y operaciones aritméticas.
'''

saldo = float(input('Ingrese el saldo inicial de la cuenta: '))

while True:
    print('\nMenú:')
    print('1. Ver Saldo')
    print('2. Depositar Dinero')
    print('3. Retirar Dinero')
    print('4. Salir')

    opcion = input('Seleccione una opción (1-4): ')

    if opcion == '1':
        print(f'Su saldo actual es: ${saldo:.2f}')
    elif opcion == '2':
        deposito = float(input('Ingrese la cantidad a depositar: $ '))
        if deposito <= 0:
            print('Debes ingresar un valor superior a 0')
        else:
            saldo += deposito
            print(f'Deposito Exitoso. Tu nuevo saldo es: ${saldo:.2f}')
    elif opcion == '3':
        retiro= float(input('Digite la catidad a retirar: $'))
        if retiro <= 0:
            print('Debes ingresar un valor superior a 0')
        elif retiro > saldo:
            print('Fondos insuficientes para realizar el retiro')
        else:
            saldo -= retiro
            print(f'Retiro Exitoso. Tu nuevo saldo es: ${saldo:.2f}')
    elif opcion == '4':
        print('Gracias por usar el cajero automático. ¡Hasta luego!')
        break
    else:
        print('Opción no válida. Por favor, seleccione una opción del 1 al 4.')



