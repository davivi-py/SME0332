import numpy as np

def f(x):
    return np.sqrt(np.maximum(0.0, 1.0 - x**2))

def riemann_vectorized(N, a, b, f):
    dx = (b - a) / N
    x = np.linspace(a, b, N+1)
    return np.sum(f(x[1:])) * dx

# Chamada correta:
resultado = riemann_vectorized(1000, 0, 1, f)
pi_aprox = 4 * resultado
print(f"π aproximado: {pi_aprox}")
print(f"π real: {np.pi}")
print(f"Erro: {abs(pi_aprox - np.pi)}")