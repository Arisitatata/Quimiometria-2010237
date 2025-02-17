def predecir_solubilidad(Kps, concentracion_ion1, concentracion_ion2):
    if Kps <= 0 or concentracion_ion1 <= 0 or concentracion_ion2 <= 0:
        raise ValueError("El Kps y las concentraciones deben ser mayores que 0")
    producto_ionico = concentracion_ion1 * concentracion_ion2
    if producto_ionico > Kps:
        return "Insoluble"
    else:
        return "Soluble"

while True:
    try:
        Kps = float(input("Introduce el valor del Kps del compuesto: "))
        concentracion_ion1 = float(input("Introduce la concentración del primer ion (en moles/litro): "))
        concentracion_ion2 = float(input("Introduce la concentración del segundo ion (en moles/litro): "))

        # Predecir la solubilidad
        solubilidad = predecir_solubilidad(Kps, concentracion_ion1, concentracion_ion2)

        # Mostrar el resultado
        print(f"El compuesto es: {solubilidad}")

        # Preguntar si el usuario desea realizar otro cálculo
        otra_vez = input("¿Quieres predecir la solubilidad de otro compuesto? (si/no): ").strip().lower()
        if otra_vez != "si":
            break

    except ValueError as e:
        print(f"Error: {e}. Por favor, introduce valores válidos.")
    except Exception as e:
        print(f"Error inesperado: {e}. Inténtalo de nuevo.")

print("¡Gracias por usar el programa!")
