def calcular_concentracion(moles, volumen):
    # Verificar si los valores de entrada son válidos
    if moles <= 0 or volumen <= 0:
        raise ValueError("Los moles y el volumen deben ser mayores que 0")
    concentracion = moles / volumen
    return concentracion

while True:
    try:
        moles = float(input("Introduce los moles del compuesto: "))
        volumen = float(input("Introduce el volumen de la solución (en litros): "))
        
        # Calcular la concentración
        concentracion = calcular_concentracion(moles, volumen)
        
        # Mostrar el resultado
        print(f"La concentración del compuesto es: {concentracion} moles/litro")

        # Preguntar si el usuario desea realizar otro cálculo
        otra_vez = input("¿Quieres calcular otra concentración? (si/no): ").strip().lower()
        if otra_vez != "si":
            break

    except ValueError as e:
        print(f"Error: {e}. Por favor, introduce valores válidos.")
    except Exception as e:
        print(f"Error inesperado: {e}. Inténtalo de nuevo.")

print("¡Gracias por usar el programa!")
