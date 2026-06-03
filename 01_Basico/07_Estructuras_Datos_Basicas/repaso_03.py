inventario = {
    "Laptop" : [800000, 5],
    "Mouse" : [25000, 20],
    "Teclado" : [75000, 10]
}

while True:
    print("Menú de opciones:")
    print("1. Ver inventario\n"
          "2. Buscar producto\n"
          "3. Añadir producto\n"
          "4. Actualizar producto\n"
          "5. Eliminar producto\n"
          "6. Salir")

    opcion = int(input("Ingrese el número de la opción deseada: "))

    if opcion == 1:
        for producto in inventario:
            print(f'{producto}: Precio: {inventario[producto][0]}, Cantidad: {inventario[producto][1]}')

    elif opcion == 2:
        producto = input("Ingrese el nombre del producto: ")
        if producto in inventario:
            print(f'{producto}: Precio: {inventario[producto][0]}, Cantidad: {inventario[producto][1]}')
        else:
            print("Producto no encontrado.")

    elif opcion == 3:
        producto = input('Ingrese el nombre del nuevo producto: ')
        if producto not in inventario:
            precio = float(input('Ingrese el precio del producto: '))
            cantidad = int(input('Ingrese la cantidad del producto: '))
            if precio >= 0 and cantidad >= 0:
                inventario[producto] = [precio, cantidad]
            else:
                print("Precio y cantidad deben ser positivos.")
        else:
            print("El producto ya existe.")

    elif opcion == 4:
        producto = input('Ingrese el nombre del producto a actualizar: ')
        if producto in inventario:
            precio = float(input('Ingrese el nuevo precio del producto: '))
            cantidad = int(input('Ingrese la nueva cantidad del producto: '))
            if precio >= 0 and cantidad >= 0:
                inventario[producto] = [precio, cantidad]
            else:
                print("Precio y cantidad deben ser positivos.")
        else:
            print("Producto no encontrado.")

    elif opcion == 5:
        producto = input('Ingrese el nombre del producto a eliminar: ')
        if producto in inventario:
            del inventario[producto]
        else:
            print("Producto no encontrado.")
