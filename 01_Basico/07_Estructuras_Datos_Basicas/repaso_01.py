lista_compras = ['Leche','Pan','Huevos','Queso','Frutas']

while True:
    print('\nMenu de Opciones:\n'
          'Opción 1: Ver lista de Completa\n'
          'Opción 2: Añadir Producto\n'
          'Opción 3: Eliminar Producto\n'
          'Opción 4: Contar Productos\n'
          'Opción 5: Salir\n')

    opcion = input('Ingrese una opción: ')
    if opcion == '1':
        print('Lista de Productos: ')
        for i,productos in enumerate(lista_compras):
            print(f'{i+1}. {productos}')
    elif opcion == '2':
        producto = input('Ingrese el nombre del producto a añadir: ')
        if producto not in lista_compras:
            lista_compras.append(producto)
        else:
            print('Producto ya existe en la lista')
    elif opcion == '3':
        producto = input('Ingrese el nombre del producto a eliminar: ')
        if producto in lista_compras:
            lista_compras.remove(producto)
        else:
            print('Producto no existe en la lista')
    elif opcion == '4':
        print(f'Número de productos en la lista: {len(lista_compras)}')
    elif opcion == '5':
        print('Saliendo del programa...')
        break
    else:
        print('Opción no válida, por favor intente de nuevo.')



