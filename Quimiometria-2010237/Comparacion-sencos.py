import math

# Función para calcular el factorial de un número
def factorial(n):
    result = 1
    for i in range(2, n + 1):  # Multiplicamos desde 2 hasta n
        result *= i
    return result

# Función para calcular la potencia de un número
def power(x, n):
    result = 1
    for _ in range(n):  # Multiplicamos x por sí mismo n veces
        result *= x
    return result

# Función para calcular el seno usando la serie de Taylor
def sine(x, terms=10):
    sin_x = 0
    for n in range(terms):  # Iteramos en la serie de Taylor hasta el número de términos deseado
        sign = (-1) ** n  # Alternamos los signos en cada término
        sin_x += sign * power(x, 2 * n + 1) / factorial(2 * n + 1)  # Fórmula de la serie
    return sin_x

# Función para calcular el coseno usando la serie de Taylor
def cosine(x, terms=10):
    cos_x = 0
    for n in range(terms):  # Iteramos en la serie de Taylor hasta el número de términos deseado
        sign = (-1) ** n  # Alternamos los signos en cada término
        cos_x += sign * power(x, 2 * n) / factorial(2 * n)  # Fórmula de la serie
    return cos_x

# Función para convertir grados a radianes
def degrees_to_radians(degrees):
    return degrees * (3.141592653589793 / 180)  # Fórmula de conversión

# Solicitamos al usuario un ángulo en grados
angle = float(input("Introduce un ángulo en grados: "))
radians = degrees_to_radians(angle)  # Convertimos el ángulo a radianes

# Calculamos seno y coseno con la serie de Taylor y con la librería math
calculated_sine = sine(radians)
calculated_cosine = cosine(radians)
math_sine = math.sin(radians)
math_cosine = math.cos(radians)

# Mostramos los resultados
print(f"Seno({angle}°) ≈ {calculated_sine} (math.sin: {math_sine})")
print(f"Coseno({angle}°) ≈ {calculated_cosine} (math.cos: {math_cosine})")

# Verificamos si los resultados son iguales
if math.isclose(calculated_sine, math_sine, rel_tol=1e-9) and math.isclose(calculated_cosine, math_cosine, rel_tol=1e-9):
    print("Los resultados de seno y coseno son iguales a los obtenidos con el módulo math.")
else:
    print("Los resultados de seno y coseno NO son iguales a los obtenidos con el módulo math.")
