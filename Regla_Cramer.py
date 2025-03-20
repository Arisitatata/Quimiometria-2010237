import numpy as np

# Constantes
A = np.array([[0.3, 0.52, 1],
              [0.5, 1, 1.9],
              [0.1, 0.3, 0.5]])
B = np.array([-0.01, 0.67, -0.44])

def cramer_rule(A, B):
    try:
        det_A = np.linalg.det(A)
        if np.isclose(det_A, 0):
            raise ValueError("La matriz A es singular y no tiene solución única.")

        # Crear matrices modificadas y calcular determinantes
        A1 = A.copy()
        A1[:, 0] = B
        det_A1 = np.linalg.det(A1)

        A2 = A.copy()
        A2[:, 1] = B
        det_A2 = np.linalg.det(A2)

        A3 = A.copy()
        A3[:, 2] = B
        det_A3 = np.linalg.det(A3)

        # Calcular soluciones
        x1 = det_A1 / det_A
        x2 = det_A2 / det_A
        x3 = det_A3 / det_A

        return x1, x2, x3
    except Exception as e:
        print(f"Error: {e}")
        return None

# Ejecución principal
if __name__ == "__main__":
    solutions = cramer_rule(A, B)
    if solutions:
        x1, x2, x3 = solutions
        print(f"x1 = {x1:.1f}, x2 = {x2:.1f}, x3 = {x3:.1f}")