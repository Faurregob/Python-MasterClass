edad = int(input("Ingrese su edad: "))
registro = input("¿Está registrado? (si/no): ").lower()
registro_booleano = registro == "si"
acepta_terminos = input("¿Acepta los términos y condiciones? (si/no): ").lower()
acepta_terminos_booleano = acepta_terminos == "si"
plan = input("Ingrese el plan que desea contratar (Gratuito / Premium / Vip): ").lower()
calificacion = float(input("Ingrese su calificación (1-10): "))


# Imprimir el mensaje final
print("\n--- Datos del Usuario ---")
print(f"Edad: {edad} años")
print(f"Registrado: {'Sí' if registro_booleano else 'No'}")
print(f"Acepta términos: {'Sí' if acepta_terminos_booleano else 'No'}")
print(f"Plan: {plan.capitalize()}")
print(f"Calificación: {calificacion}")

if edad < 13:
    mensaje = "Rechazado: muy joven para acceder"
elif not registro_booleano :
    mensaje = "Rechazado: debe registrarse para acceder"
elif not acepta_terminos_booleano:
    mensaje = "Rechazado: debe aceptar los términos y condiciones para acceder"
elif plan == "gratuito" and calificacion < 7.0:
    mensaje = "Rechazado: plan gratuito requiere calificación >= 7.0"
elif plan == "vip":
    mensaje = "Acceso permitido: Bienvenido VIP"
elif plan == "premium" and (edad >= 18 or calificacion >= 8.0):
    mensaje = "Acceso permitido: bienvenido Premium"
else:
    mensaje = "Rechazado: no cumple con los requisitos para el plan seleccionado"

print(f"\nResultado: {mensaje}")




