import datetime
#"Ino estoy utilizando el modulo datetime actualmente"
#"mas delante lo utilizare para detectar las semanas automaticamente"

INGRESO_MENSUAL = float(input("¿Cuál es tu ingreso mensual? $"))
#"preguntar y obetener el ingreso mensual"
#"Lo convierte a número decimal (float), porque el input devuelve texto (str)."

limite_semanal = INGRESO_MENSUAL / 4.33
#"el presupuesto semanal se adquiere"
#"dividiendo tu ingreso mensual por 4.33 (porque un mes tiene en promedio 4.33 semanas)."
#"Si ganás $120.000 al mes, tu límite semanal será ~$27.700."

gastos_semana = []
total_gastado = 0
#"Una lista vacía gastos_semana, donde se guardarán los gastos semanales"
#"personales del usuario."
#"Una variable total_gastado que va sumando el total gastado en la semana."

print(f"Tu límite semanal es: ${limite_semanal:.2f}")

while True:
    gasto = input("Ingresá un gasto (o escribí 'salir'): ")
#    "Este es un bucle que se repite hasta que escribís salir"
#    "Cada vez que escribís un número, se guarda como un gasto nuevo"


    if gasto.lower() == "salir":
        break
    try:
        gasto = float(gasto)
#        "Intenta convertir el gasto ingresado a número decimal."

        gastos_semana.append(gasto)
        total_gastado = sum(gastos_semana)
#        "Agrega el gasto a la lista gastos_semana"
#        "Calcula la suma total de gastos hasta ahora usando sum(...)"

        restante = limite_semanal - total_gastado
        if restante < 0:
            print(f"🚨 Te pasaste del límite semanal por ${-restante:.2f}!")
        else:
            print(f"Te quedan ${restante:.2f} esta semana.")
    except ValueError:
        print("Entrada inválida. Ingresá un número.")
