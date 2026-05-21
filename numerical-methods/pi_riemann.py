"""
π Approximation via Riemann Integration
=========================================
Approximates π by integrating sqrt(1 - x²) over [0, 1] using Riemann sums.
Plots convergence and absolute error as functions of N on a log-log scale.

Usage:
    python pi_riemann.py
"""

import numpy as np
import matplotlib.pyplot as plt


def f(x):
    return np.sqrt(np.maximum(0.0, 1.0 - x**2))


def riemann(N, a, b, func):
    """Estimate definite integral using a right Riemann sum with N subdivisions."""
    dx = (b - a) / N
    x = np.linspace(a, b, N + 1)
    return np.sum(func(x[1:])) * dx


if __name__ == "__main__":
    result = riemann(1000, 0, 1, f)
    pi_approx = 4 * result
    print(f"π approx: {pi_approx}")
    print(f"π real:   {np.pi}")
    print(f"Error:    {abs(pi_approx - np.pi)}")

    ns = [10**3, 10**4, 10**5, 10**6]
    errors = [abs(4 * riemann(n, 0, 1, f) - np.pi) for n in ns]
    pi_values = [4 * riemann(n, 0, 1, f) for n in ns]

    plt.figure(figsize=(12, 5))

    plt.subplot(1, 2, 1)
    plt.plot(ns, pi_values, marker="o", color="blue", label="π approx")
    plt.axhline(y=np.pi, color="red", linestyle="--", label="π real")
    plt.xscale("log")
    plt.xlabel("Subdivisions (N)")
    plt.ylabel("π value")
    plt.title("Convergence of π approximation")
    plt.legend()
    plt.grid(True, alpha=0.3)

    plt.subplot(1, 2, 2)
    plt.plot(ns, errors, marker="o", color="red")
    plt.xscale("log")
    plt.yscale("log")
    plt.xlabel("Subdivisions (N)")
    plt.ylabel("Absolute error")
    plt.title("Error vs N (log-log scale)")
    plt.grid(True, alpha=0.3)

    plt.tight_layout()
    plt.show()
