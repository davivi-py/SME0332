import numpy as np


def jacobi_general(A, b, x0, epsilon, max_iter=10000):
    A = np.array(A, dtype=float)
    b = np.array(b, dtype=float)
    x = np.array(x0, dtype=float)
    n = len(b)

    for k in range(1, max_iter + 1):
        x_new = np.zeros_like(x)

        for i in range(n):
            soma = 0.0
            for j in range(n):
                if j != i:
                    soma += A[i, j] * x[j]
            x_new[i] = (b[i] - soma) / A[i, i]

        erro = np.max(np.abs(x_new - x))

        x = x_new

        if erro < epsilon:
            return x, k

    return x, max_iter


def main():
    A = [
        [3, -1, -1],
        [-1, 3, -1],
        [-1, -1, 3],
    ]
    b = [1, 2, 3]

    x0 = [0.0, 0.0, 0.0]
    epsilon = 1e-6

    x_sol, k = jacobi_general(A, b, x0, epsilon)

    print("Solução aproximada:")
    for i, xi in enumerate(x_sol, start=1):
        print(f"x_{i} ≈ {xi:.6f}")
    print(f"Número de iterações: {k}")


if __name__ == "__main__":
    main()