"""
Monte Carlo Area Estimation
============================
Estimates the area between two curves f(x) and g(x) using Monte Carlo sampling,
and compares the result against numerical Riemann integration.

Usage:
    python monte_carlo_area.py
"""

import numpy as np
import matplotlib.pyplot as plt


def f(x):
    return 1 + 0.5 * np.sin(2 * x) ** 3


def g(x):
    return 3 + 0.5 * np.cos(3 * x) ** 5


if __name__ == "__main__":
    N = 10000
    x = np.linspace(0, 2 * np.pi, N)
    dx = (2 * np.pi) / N

    area_riemann = np.sum(g(x) - f(x)) * dx
    print(f"Riemann area: {area_riemann:.6f}")

    x_rand = np.random.uniform(0, 2 * np.pi, N)
    y_rand = np.random.uniform(0, 4, N)

    inside = (y_rand >= np.minimum(f(x_rand), g(x_rand))) & \
             (y_rand <= np.maximum(f(x_rand), g(x_rand)))
    outside = ~inside

    area_mc = (2 * np.pi * 4) * np.sum(inside) / N
    print(f"Monte Carlo area: {area_mc:.6f}")

    plt.figure(figsize=(10, 6))
    plt.plot(x, f(x), label="f(x)", color="blue")
    plt.plot(x, g(x), label="g(x)", color="red")
    plt.scatter(x_rand[inside], y_rand[inside], color="green", s=1, alpha=0.5, label="Inside")
    plt.scatter(x_rand[outside], y_rand[outside], color="red", s=1, alpha=0.2, label="Outside")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.title("Area Between Curves — Monte Carlo")
    plt.legend()
    plt.grid(True)
    plt.show()
