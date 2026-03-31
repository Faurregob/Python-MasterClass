edad = int(input("Por favor ingresa la edad del Usuario: "))
dinero_disponible = float(input("Por favor ingresa el dinero disponible del Usuario: "))
miembro_vip = input("¿El Usuario es miembro VIP? (si/no): ").strip().lower()
invitacion = input("¿El Usuario tiene una invitación? (si/no): ").strip().lower()

#Imprime Datos del Usuario
print("\nDatos del Usuario:")
print(f"Edad: {edad} años")
print(f"Dinero Disponible: ${dinero_disponible:.2f}")
print(f"Miembro VIP: {'Sí' if miembro_vip == 'si' else 'No'}")
print(f"Invitación: {'Sí' if invitacion == 'si' else 'No'}")


if edad < 18:
    print("Acceso denegado: Es menor de edad.")
elif miembro_vip == "si":
    print("Acceso permitido: eres VIP")
elif invitacion == "si" and dinero_disponible >= 50000:
    print("Acceso permitido: tienes invitación y suficiente dinero.")
elif edad >= 25 and dinero_disponible >= 100000:
    print("Acceso permitido: eres mayor de edad y tienes suficiente dinero.")
else:
    print("Acceso denegado: No cumples con los requisitos.")

