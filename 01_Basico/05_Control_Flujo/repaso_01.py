contrasena = input("Por favor ingrese una contraseña: ")
enmascarada = "*" * len(contrasena)
print(f"Su contraseña es: {enmascarada}")

if "password" in contrasena.lower() or "123456" in contrasena:
    fortaleza = "Muy debil"
elif len(contrasena) < 8:
    fortaleza = "Debil."
elif len(contrasena) <= 11:
    fortaleza = "Media."
elif len(contrasena) >= 12 and any(char.isdigit() for char in contrasena) and any(char.isupper() for char in contrasena):
    fortaleza = "Fuerte."
else:
    fortaleza = "Media."


print("¡Gracias por usar nuestro sistema de contraseñas!\n"
      f"Contraseña ingresada: {enmascarada}\n"
      f"Longitud de la contraseña: {len(contrasena)} caracteres\n"
      f"Fortaleza: {fortaleza}")


