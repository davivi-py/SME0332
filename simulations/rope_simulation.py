"""
Rope Under Gravity — Jacobi & Gauss-Seidel Solvers
====================================================
Models the equilibrium shape of a rope with variable linear density under gravity.
Compares Jacobi and Gauss-Seidel convergence across grid refinements (N = 10, 20, 40, 80).

Usage:
    python rope_simulation.py
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad

L = 1.0   # rope length
TAU = 2.0 # tension
G = 9.81  # gravity


def rho_uniform(x):
    """Uniform linear density."""
    return 1.0


def rho_variable(x):
    """Variable density with a Gaussian bump at x=0.5."""
    return 0.5 * (1 + np.exp(-100 * (x - 0.5) ** 2))


def compute_masses(N, density_func):
    """Compute discrete nodal masses by integrating the density function."""
    l0 = L / N
    masses = np.zeros(N + 1)
    masses[0], _ = quad(density_func, 0, 0.5 * l0)
    masses[N - 1], _ = quad(density_func, L - 0.5 * l0, L)
    for i in range(1, N - 1):
        masses[i], _ = quad(density_func, (i - 0.5) * l0, (i + 0.5) * l0)
    return masses


def jacobi_solver(masses, num_iter=5000, tol=1e-7):
    """Solve for equilibrium shape using the Jacobi iterative method."""
    N = len(masses) - 1
    l0 = L / N
    y_old = np.zeros(N + 1)
    y_new = np.zeros(N + 1)
    for _ in range(num_iter):
        for i in range(1, N):
            y_new[i] = 0.5 * (y_old[i - 1] + y_old[i + 1]) - (l0 * masses[i] * G / (2 * TAU))
        y_old = y_new.copy()
    return y_new


def gauss_seidel_solver(masses, num_iter=5000, tol=1e-7):
    """Solve for equilibrium shape using the Gauss-Seidel iterative method."""
    N = len(masses) - 1
    l0 = L / N
    y = np.zeros(N + 1)
    for _ in range(num_iter):
        y_old = y.copy()
        for i in range(1, N):
            y[i] = 0.5 * (y[i - 1] + y[i + 1]) - (l0 * masses[i] * G / (2 * TAU))
        if np.max(np.abs(y - y_old)) < tol:
            return y
    return y


if __name__ == "__main__":
    grid_sizes = [10, 20, 40, 80]
    density_cases = [("Uniform density", rho_uniform), ("Variable density", rho_variable)]
    solvers = [("Jacobi", jacobi_solver), ("Gauss-Seidel", gauss_seidel_solver)]

    plt.figure(figsize=(14, 10))
    plot_idx = 1

    for (solver_name, solver) in solvers:
        for (density_name, density_func) in density_cases:
            plt.subplot(2, 2, plot_idx)
            for N in grid_sizes:
                masses = compute_masses(N, density_func)
                y = solver(masses)
                x = np.linspace(0, L, N + 1)
                plt.plot(x, y, label=f"N={N}")
            plt.title(f"{density_name} ({solver_name})")
            plt.xlabel("X")
            plt.ylabel("Y")
            plt.grid(True)
            plt.legend()
            plot_idx += 1

    plt.tight_layout()
    plt.show()
