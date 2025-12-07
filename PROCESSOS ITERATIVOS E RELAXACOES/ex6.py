import numpy as np
import matplotlib.pyplot as plt


def f(x):
    return x * np.exp(-x**2) - 0.1


def df(x):
    return np.exp(-x**2) * (1 - 2 * x**2)


def newton_method(x0, epsilon, max_iter=1000):
    x = x0

    for k in range(1, max_iter + 1):
        if abs(df(x)) < 1e-10:
            print(f"Aviso: derivada ~0 em x = {x:.6f}")
            return x, k

        x_new = x - f(x) / df(x)

        if abs(x_new - x) < epsilon:
            return x_new, k

        x = x_new

    print(f"Aviso: não convergiu em {max_iter} iterações para x0 = {x0:.2f}")
    return x, max_iter


def main():
    x_vals = np.linspace(-1, 2, 400)
    y_vals = f(x_vals)

    plt.figure(figsize=(8, 5))
    plt.plot(x_vals, y_vals, label=r"$f(x) = x e^{-x^2} - 0.1$")
    plt.axhline(0, color="black", linewidth=0.8, linestyle="--")
    plt.axvline(0, color="black", linewidth=0.8, linestyle="--")
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.title("f(x) = x e^{-x^2} - 0.1")
    plt.grid(True, alpha=0.3)
    plt.legend()
    plt.show()

    x0_raiz1 = 0.15
    x0_raiz2 = 1.5
    epsilon = 1e-8

    print(f"\n--- Raiz 1 (x0 = {x0_raiz1}) ---")
    raiz1, iter1 = newton_method(x0_raiz1, epsilon)
    print(f"Raiz 1 ≈ {raiz1:.8f}")
    print(f"Iterações: {iter1}")
    print(f"f(raiz1) = {f(raiz1):.2e}")

    print(f"\n--- Raiz 2 (x0 = {x0_raiz2}) ---")
    raiz2, iter2 = newton_method(x0_raiz2, epsilon)
    print(f"Raiz 2 ≈ {raiz2:.8f}")
    print(f"Iterações: {iter2}")
    print(f"f(raiz2) = {f(raiz2):.2e}")


if __name__ == "__main__":
    main()