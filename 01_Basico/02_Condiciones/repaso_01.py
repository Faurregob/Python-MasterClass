contrasena = "Admin1234"
pass_user = input("Por favor ingrese una contraseña: ")
if len(pass_user) < 8:
    print("Estas ingresando menor a 8 caracteres")
elif pass_user != contrasena:
    print("Contraseña Invalida.")
else:
    print("Bienvenido")