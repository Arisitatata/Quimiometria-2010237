def calcular_rendimiento_teorico(rendimiento_real, rendimiento_teorico):
    if rendimiento_real <= 0 or rendimiento_teorico <= 0:
        raise ValueError("El rendimiento real y el rendimiento teórico deben ser mayores que 0")
    rendimiento_teorico_calculado = (rendimiento_real / rendimiento_teorico) * 100
    return rendimiento_teorico_calculado

while True:
    try:
        rendimiento_real = float(input("Introduce el rendimiento real de la reacción (en gramos): "))
        rendimiento_teorico = float(input("Introduce el rendimiento teórico de la reacción (en gramos): "))

        # Calcular el rendimiento teórico
        rendimiento_teorico_calculado = calcular_rendimiento_teorico(rendimiento_real, rendimiento_teorico)

        # Mostrar el resultado
        print(f"El rendimiento teórico de la reacción es: {rendimiento_teorico_calculado}%")

        # Preguntar si el usuario desea realizar otro cálculo
        otra_vez = input("¿Quieres calcular otro rendimiento teórico? (si/no): ").strip().lower()
        if otra_vez != "si":
            break

    except ValueError as e:
        print(f"Error: {e}. Por favor, introduce valores válidos.")
    except Exception as e:
        print(f"Error inesperado: {e}. Inténtalo de nuevo.")

print("¡Gracias por usar el programa!")

