import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return 1 + 0.5 * np.sin(2 * x)**3

def g(x):
    return 3 + 0.5 * np.cos(3 * x)**5

N = 10000

x_plot = np.linspace(0, 2 * np.pi, N) # Renomeado para evitar conflito com x_rand
delta_x = (2 * np.pi) / N

area_f = np.sum(f(x_plot)) * delta_x
area_g = np.sum(g(x_plot)) * delta_x
area_riemann = area_g - area_f

print(f"Área pela soma de Riemann: {area_riemann:.6f}")

# Monte Carlo
x_rand = np.random.uniform(0, 2 * np.pi, N)
y_rand = np.random.uniform(0, 4, N)

f_x_rand = f(x_rand)
g_x_rand = g(x_rand)

# Condição para pontos DENTRO da região
dentro = (y_rand >= np.minimum(f_x_rand, g_x_rand)) & \
(y_rand <= np.maximum(f_x_rand, g_x_rand))

# Condição para pontos FORA da região (explícita)
fora = (y_rand < np.minimum(f_x_rand, g_x_rand)) | \
       (y_rand > np.maximum(f_x_rand, g_x_rand))

area_retangulo = 2 * np.pi * 4
area_mc = area_retangulo * np.sum(dentro) / N

print(f"Área pelo Monte Carlo: {area_mc:.6f}")

plt.figure(figsize=(10, 6))
plt.plot(x_plot, f(x_plot), label='f(x)', color='blue')
plt.plot(x_plot, g(x_plot), label='g(x)', color='red')
plt.scatter(x_rand[dentro], y_rand[dentro], color='green', s=1, alpha=0.5, label='Pontos dentro')
plt.scatter(x_rand[fora], y_rand[fora], color='red', s=1, alpha=0.5, label='Pontos fora') # Usando 'fora' explícito
plt.xlabel('x')
plt.ylabel('y')
plt.title('Área entre as curvas')
plt.legend()
plt.grid(True)
plt.show()