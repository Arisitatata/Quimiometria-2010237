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

# Función para determinar si seno y coseno son iguales
def check_equal_sine_cosine(angle):
    radians = degrees_to_radians(angle)
    sin_value = sine(radians)
    cos_value = cosine(radians)
    return math.isclose(sin_value, cos_value, rel_tol=1e-6)

# Solicitar un ángulo al usuario
angle = float(input("Introduce un ángulo en grados: "))
if check_equal_sine_cosine(angle):
    print(f"El seno y el coseno de {angle}° son aproximadamente iguales.")
else:
    print(f"El seno y el coseno de {angle}° no son iguales.")

