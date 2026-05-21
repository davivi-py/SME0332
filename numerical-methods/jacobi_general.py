"""
Jacobi Iterative Solver — General n×n Systems
===============================================
Solves diagonally dominant linear systems Ax = b using the Jacobi method.
Stops when the max absolute change between iterations falls below epsilon.

Usage:
    python jacobi_general.py
"""

import numpy as np


def jacobi_solve(A, b, x0, epsilon, max_iter=10000):
    """
    Solve Ax = b iteratively using the Jacobi method.

    Args:
        A: Coefficient matrix (n×n), must be diagonally dominant.
        b: Right-hand side vector (n,).
        x0: Initial guess (n,).
        epsilon: Convergence tolerance.
        max_iter: Maximum number of iterations.

    Returns:
        (x, k): Solution vector and number of iterations used.
    """
    A = np.array(A, dtype=float)
    b = np.array(b, dtype=float)
    x = np.array(x0, dtype=float)
    n = len(b)

    for k in range(1, max_iter + 1):
        x_new = np.zeros_like(x)
        for i in range(n):
            off_diag = sum(A[i, j] * x[j] for j in range(n) if j != i)
            x_new[i] = (b[i] - off_diag) / A[i, i]

        if np.max(np.abs(x_new - x)) < epsilon:
            return x_new, k
        x = x_new

    return x, max_iter


if __name__ == "__main__":
    A = [[3, -1, -1], [-1, 3, -1], [-1, -1, 3]]
    b = [1, 2, 3]
    x0 = [0.0, 0.0, 0.0]

    x_sol, k = jacobi_solve(A, b, x0, epsilon=1e-6)

    print("Approximate solution:")
    for i, xi in enumerate(x_sol, start=1):
        print(f"  x_{i} ≈ {xi:.6f}")
    print(f"Iterations: {k}")
