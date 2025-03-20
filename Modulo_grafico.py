import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import fsolve

# Constantes
MASS = 68.1           # kg
GRAVITY = 9.81        # m/s^2
TIME = 10             # s
TARGET_VELOCITY = 40  # m/s

# Definición de la función f(c)
def f(c):
    try:
        return (MASS * GRAVITY / c) * (1 - np.exp(-c * TIME / MASS)) - TARGET_VELOCITY
    except ZeroDivisionError:
        return np.inf  # Retorna infinito si hay división por cero

# Función para graficar f(c)
def plot_function():
    c_vals = np.linspace(0.1, 20, 500)
    f_vals = f(c_vals)

    plt.figure(figsize=(8, 5))
    plt.plot(c_vals, f_vals, label=r'$f(c)=\frac{m\,g}{c}(1-e^{-ct/m})-40$')
    plt.axhline(0, color='red', linestyle='--')
    plt.xlabel('c [N·s/m]')
    plt.ylabel('f(c)')
    plt.title('Determinación gráfica del coeficiente de resistencia')
    plt.legend()
    plt.grid(True)
    plt.show()

# Función para resolver numéricamente usando fsolve
def solve_numerically():
    try:
        c_sol = fsolve(f, 15)  # semilla cercana a 15
        print(f"El valor aproximado de c es: {c_sol[0]:.4f} N·s/m")
    except Exception as e:
        print(f"Error al resolver numéricamente: {e}")

# Ejecución principal
if __name__ == "__main__":
    plot_function()
    solve_numerically()