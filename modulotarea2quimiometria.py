import math

def calculoph():
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

def calculomoles():
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

def calculoconcentracion():
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

def calculorendimiento():
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

def calculophbuffer():
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

def calculosolubilidad():
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