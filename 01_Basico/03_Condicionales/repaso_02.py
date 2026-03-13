contrasena = input("Ingrese su contraseña: ")
mensaje1 = "fuerte" if len(contrasena) >= 12 else "débil"
mensaje2 = any(char.isdigit() for char in contrasena)
mensaje3 = "0" in contrasena or "1" in contrasena or "2" in contrasena
print(f"La contraseña posee {len(contrasena)} caracteres y es una contraseña: {mensaje1}\n"
      f"La contraseña posee numeros '0, 1, 2': {mensaje2}\n"
      f"La contraseña posee numeros '0, 1, 2': {mensaje3}\n")
