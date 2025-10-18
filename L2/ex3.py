import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return np.sqrt(np.maximum(0.0, 1.0 - x**2))

def riemann_vectorized(N, a, b, f):
    dx = (b - a) / N
    x = np.linspace(a, b, N+1)
    return np.sum(f(x[1:])) * dx


resultado = riemann_vectorized(1000, 0, 1, f)
pi_aprox = 4 * resultado
print(f"π aproximado: {pi_aprox}")
print(f"π real: {np.pi}")
print(f"Erro: {abs(pi_aprox - np.pi)}")


lista_n = [10**3, 10**4, 10**5, 10**6]
lista_erros = []
lista_piaprox = []

for n in lista_n:
    soma_riemann = riemann_vectorized(n, 0, 1, f)
    pi_aprox = 4 * soma_riemann  
    erro = abs(pi_aprox - np.pi)
    
    lista_piaprox.append(pi_aprox)
    lista_erros.append(erro)

plt.figure(figsize=(12, 5))

plt.subplot(1, 2, 1)
plt.plot(lista_n, lista_piaprox, marker='o', color='blue', label='π aproximado')
plt.axhline(y=np.pi, color='red', linestyle='--', label='π real')
plt.xscale('log')
plt.xlabel('Número de subdivisões (N)')
plt.ylabel('Valor de π')
plt.title('Convergência da aproximação de π')
plt.legend()
plt.grid(True, alpha=0.3)

# Gráfico 2: Erro absoluto vs N
plt.subplot(1, 2, 2)
plt.plot(lista_n, lista_erros, marker='o', color='red', label='Erro absoluto')
plt.xscale('log')
plt.yscale('log')
plt.xlabel('Número de subdivisões (N)')
plt.ylabel('Erro absoluto')
plt.title('Erro em função de N (escala log-log)')
plt.legend()
plt.grid(True, alpha=0.3)

plt.tight_layout()
plt.show()