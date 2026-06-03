salario_base = float(input("Ingrese su salario base mensual: "))
tiempo_laborado = int(input("Ingrese los años que laboro en la empresa: "))
proyectos = int(input("Ingrese el número de proyectos exitosos: "))
calificacion = float(input("Ingrese su calificación de desempeño (1-5): "))
tiene_licencia = input("¿Tiene licencia de conducir? (si/no): ").lower() == "si"
tiene_certificaciones = input("¿Tiene certificaciones profesionales? (si/no): ").lower() == "si"
asistencia = float(input("Ingrese su porcentaje de asistencia mensual (0-100): "))

if salario_base < 1000000:
    exit("Salario muy bajo para recibir bonificación")
elif asistencia < 60:
    exit("Rechazado: asistencia insuficiente para recibir bonificación")
else:
    porcentaje = 0

    if calificacion < 3.0:
        porcentaje += 0
    elif calificacion >= 3.0:
        porcentaje += 5

    # Incremento por años laborados Maximo 20 años
    porcentaje += min(tiempo_laborado, 20)

    if proyectos >= 20:
        porcentaje += 10
    elif proyectos >= 10:
        porcentaje += 5

    if tiene_certificaciones == True:
        porcentaje += 3

    if asistencia < 70:
        porcentaje -= 10
    elif asistencia < 80:
        porcentaje -= 5

    if porcentaje < 0:
        porcentaje = 0

    bonificacion = salario_base * (porcentaje / 100)
    salario_total = salario_base + bonificacion
    incremento_proyectos = 10 if proyectos >= 20 else (5 if proyectos >= 10 else 0)
    penalidad_asistencia = -10 if asistencia < 70 else (-5 if asistencia < 80 else 0)

    print("\n--- Datos del Empleado ---")
    print(f"\nDesglose de bonificación:")
    print(f"- Base (desempeño >= 3): 5%")
    print(f"- Incremento por años ({tiempo_laborado}): +{min(tiempo_laborado, 20)}%")
    print(f"- Incremento por proyectos ({proyectos}): +{incremento_proyectos}%")
    print(f"- Incremento por certificaciones: +{3 if tiene_certificaciones else 0}%")
    print(f"- Penalidad por asistencia: {penalidad_asistencia}%")
    print(f"\nTotal bonificación: {porcentaje}%")
    print(f"\nMonto bonificación: ${bonificacion:,.0f}")
    print(f"Salario total: ${salario_total:,.0f}")