import numpy as np
import matplotlib.pyplot as plt

n = 20

pontos = np.zeros(n)

def phi(x):
    return (1/(x**0.5))

x0 = 0.75
pontos[0] = x0

for i in range(1, n):
    x1 = phi(x0)
    pontos[i] = x1
    x0 = x1

fig, ax = plt.subplots(figsize=(10, 8))

x = np.linspace(0.5, 1.4, 1000)
y_phi = phi(x)
ax.plot(x, y_phi, 'b-', linewidth=2, label='φ(x) = 1/√x')

ax.plot(x, x, 'k--', linewidth=2, label='y = x')

x_atual = pontos[0]
for i in range(1, min(len(pontos), 8)):
    y_atual = phi(x_atual)
    
    ax.plot([x_atual, x_atual], [x_atual, y_atual], 'r-', linewidth=1.5)
    ax.plot([x_atual, y_atual], [y_atual, y_atual], 'r-', linewidth=1.5)
    ax.plot(x_atual, y_atual, 'ro', markersize=5)
    
    x_atual = y_atual

ax.set_xlim(0.5, 1.4)
ax.set_ylim(0.5, 1.4)
ax.set_xlabel('x', fontsize=12)
ax.set_ylabel('y', fontsize=12)
ax.set_title('Fixed-Point Iteration for φ(x) = 1/√x', fontsize=14)
ax.grid(True, alpha=0.3)
ax.legend(fontsize=11)
ax.set_aspect('equal')

plt.tight_layout()
plt.show()