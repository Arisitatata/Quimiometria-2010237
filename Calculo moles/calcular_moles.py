# Función para calcular los moles
def calcular_moles(masa, masa_molar):
    moles = masa / masa_molar
    return moles

while True:
    try:
        # Solicitar datos al usuario
        masa = float(input("Introduce la masa del compuesto (en gramos): "))
        masa_molar = float(input("Introduce la masa molar del compuesto (en g/mol): "))

        # Calcular los moles
        moles = calcular_moles(masa, masa_molar)

        # Mostrar el resultado
        print(f"Los moles del compuesto son: {moles}")

        # Preguntar si el usuario desea realizar otro cálculo
        otra_vez = input("¿Quieres calcular otros moles? (si/no): ").strip().lower()
        if otra_vez != "si":
            break

    except ValueError as e:
        print(f"Error: {e}. Por favor, introduce valores válidos.")
    except Exception as e:
        print(f"Error inesperado: {e}. Inténtalo de nuevo.")

print("¡Gracias por usar el programa!")
