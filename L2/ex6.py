import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def calc_pi_loop(N):
    count_in = 0
    x_in, y_in, z_in = [], [], []
    x_out, y_out, z_out = [], [], []

    for _ in range(N):
        x = np.random.uniform(-1, 1)
        y = np.random.uniform(-1, 1)
        z = np.random.uniform(-1, 1)

        if x**2 + y**2 + z**2 <= 1.0:
            count_in += 1
            x_in.append(x)
            y_in.append(y)
            z_in.append(z)
        else:
            x_out.append(x)
            y_out.append(y)
            z_out.append(z)

    pi_est = 6 * count_in / N
    return pi_est, x_in, y_in, z_in, x_out, y_out, z_out

N = 1000000
pi_est, x_in, y_in, z_in, x_out, y_out, z_out = calc_pi_loop(N)

fig = plt.figure(figsize=(10, 10))
ax = fig.add_subplot(111, projection='3d')

ax.scatter(x_in, y_in, z_in, color='red', s=1, alpha=1, label='Dentro da esfera')
ax.scatter(x_out, y_out, z_out, color='blue', s=0.3, alpha=0.1, label='Fora da esfera')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('Monte Carlo 3D para π (com loop)')
ax.legend()

plt.show()