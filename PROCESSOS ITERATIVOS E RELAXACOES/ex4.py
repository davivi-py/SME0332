def jacobi_3x3(x0, y0, z0, epsilon, max_iter=10000):
    x = x0
    y = y0
    z = z0

    for k in range(1, max_iter + 1):
        x_new = (1 + y + z) / 3
        y_new = (2 + x + z) / 3
        z_new = (3 + x + y) / 3

        erro = max(
            abs(x_new - x),
            abs(y_new - y),
            abs(z_new - z)
        )

        x, y, z = x_new, y_new, z_new

        if erro < epsilon:
            return x, y, z, k

    return x, y, z, max_iter


def main():
    x0 = 0.0
    y0 = 0.0
    z0 = 0.0
    epsilon = 1e-6

    x_sol, y_sol, z_sol, k = jacobi_3x3(x0, y0, z0, epsilon)

    print(f"Solucão aproximada:")
    print(f"x ≈ {x_sol:.6f}")
    print(f"y ≈ {y_sol:.6f}")
    print(f"z ≈ {z_sol:.6f}")
    print(f"Número de iterações: {k}")


if __name__ == "__main__":
    main()