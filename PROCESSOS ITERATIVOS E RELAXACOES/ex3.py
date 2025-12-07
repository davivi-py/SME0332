import matplotlib.pyplot as plt

def jacobi_2x2(x0, y0, epsilon, max_iter=10000):
    x = x0
    y = y0

    for k in range(1, max_iter + 1):
        x_new = (2 + y) / 3
        y_new = (1 + 2 * x) / 4

        erro = max(abs(x_new - x), abs(y_new - y))

        x, y = x_new, y_new

        if erro < epsilon:
            return x, y, k

    return x, y, max_iter


def main():
    x0, y0 = 0.0, 0.0
    epsilons = [10**(-p) for p in range(2, 9)]
    iteracoes = []

    for eps in epsilons:
        x_sol, y_sol, k = jacobi_2x2(x0, y0, eps)
        iteracoes.append(k)

    plt.figure(figsize=(8, 5))
    plt.plot(epsilons, iteracoes, "o-", linewidth=2, markersize=8)
    plt.xscale("log")
    plt.xlabel("Erro(log)")
    plt.ylabel("Número de iterações")
    plt.title("Método de Jacobi")
    plt.grid(True, alpha=0.3)
    plt.show()


if __name__ == "__main__":
    main()