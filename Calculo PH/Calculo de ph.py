import math

while True:
    try:
        # Solicitar al usuario la concentración de H+
        concentracion_h = float(input("Introduce la concentración de H+ (en moles/litro): "))

        if concentracion_h <= 0:
            raise ValueError("La concentración de H+ debe ser positiva.")
        else:
            ph = -math.log10(concentracion_h)
            print(f"ph={ph}")

        # Preguntar si el usuario desea realizar otro cálculo
        otra_vez = input("¿Quieres calcular otro ph? (si/no): ").strip().lower()
        if otra_vez != "si":
            break

    except ValueError as e:
        print(f"Error: {e}. Por favor, introduce valores válidos.")
    except Exception as e:
        print(f"Error inesperado: {e}. Inténtalo de nuevo.")

print("¡Gracias por usar el programa!")
