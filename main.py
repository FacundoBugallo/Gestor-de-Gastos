from datetime import datetime

INGRESO_MENSUAL = float(input("¿Cuál es tu ingreso mensual? $"))
RESERVA_MENSUAL = float(input("¿Cuanto vas a reservar? $"))
limite_semanal = (INGRESO_MENSUAL - RESERVA_MENSUAL) / 4 
gastos_semana = []
total_gastado = 0

print(f"Tu límite semanal es: ${limite_semanal:.2f}")
print("Puedes salir escribiendo 'salir'")

while True:
    entrada = input("Ingresá un gasto o revisa tu 'historial': ")
    if entrada.lower() == "salir":
        break

    elif entrada.lower() == "historial":
        if not gastos_semana:
            print(f"No realizaste ningun gasto")
        else:
            print("Tu historial de Gastos:")
            for i, (monto, fecha) in enumerate(gastos_semana, start=1):
                print(f"{i}. ${monto:.2f} - {fecha}")
        continue

    try:
        gasto = float(entrada)
        fecha_actual = datetime.now().strftime("%d/%m/%Y %H:%M")
        gastos_semana.append((gasto, fecha_actual))
        total_gastado = sum(g[0] for g in gastos_semana)
        restante = limite_semanal - total_gastado
        
        if restante < 0:
            print(f"🚨 Te pasaste del límite semanal por ${-restante:.2f}!")
        else:
            print(f"Te quedan ${restante:.2f} esta semana.")
    except ValueError:
        print("Entrada inválida. Ingresá un número.")
