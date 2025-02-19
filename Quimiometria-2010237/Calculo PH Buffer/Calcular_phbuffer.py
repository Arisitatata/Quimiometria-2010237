import math

def calcular_pH(conc_acido, conc_base, pKa):
    # Verificar si los valores de entrada son válidos
    if conc_acido <= 0 or conc_base <= 0:
        raise ValueError("Las concentraciones deben ser mayores que 0")
    pH = pKa + math.log10(conc_base / conc_acido)
    return pH

while True:
    try:
        conc_acido = float(input("Introduce la concentración del ácido débil (en moles/litro): "))
        conc_base = float(input("Introduce la concentración de la base conjugada (en moles/litro): "))
        pKa = float(input("Introduce el valor de pKa del ácido débil: "))

        # Calcular el pH
        pH = calcular_pH(conc_acido, conc_base, pKa)

        # Mostrar el resultado
        print(f"El pH de la solución tampón es: {pH}")

        # Preguntar si el usuario desea realizar otro cálculo
        otra_vez = input("¿Quieres calcular otro pH? (si/no): ").strip().lower()
        if otra_vez != "si":
            break

    except ValueError as e:
        print(f"Error: {e}. Por favor, introduce valores válidos.")
    except Exception as e:
        print(f"Error inesperado: {e}. Inténtalo de nuevo.")

print("¡Gracias por usar el programa!")
