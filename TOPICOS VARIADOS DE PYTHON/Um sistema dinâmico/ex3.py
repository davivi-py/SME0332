import numpy as np
import matplotlib.pyplot as plt


m1 = 1.0
m2 = 1.0

dados = np.loadtxt('evol.txt')

t = dados[:, 0]
r1_x = dados[:, 1]
r1_y = dados[:, 2]
v1_x = dados[:, 3]
v1_y = dados[:, 4]
r2_x = dados[:, 5]
r2_y = dados[:, 6]
v2_x = dados[:, 7]
v2_y = dados[:, 8]

K = 0.5 * m1 * (v1_x**2 + v1_y**2) + 0.5 * m2 * (v2_x**2 + v2_y**2)

plt.figure(figsize=(12, 5))

plt.subplot(1, 2, 1)
plt.plot(r1_x, r1_y, label='Corpo 1')
plt.plot(r2_x, r2_y, label='Corpo 2')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Trajetórias')
plt.legend()
plt.axis('equal')
plt.grid(True)

plt.subplot(1, 2, 2)
plt.plot(t, K)
plt.xlabel('Tempo')
plt.ylabel('K(t)')
plt.title('Energia Cinética')
plt.grid(True)

plt.tight_layout()
plt.show()