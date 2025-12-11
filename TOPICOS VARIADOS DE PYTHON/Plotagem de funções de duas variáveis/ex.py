import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


def f(x, y):
    return np.cos(x) * np.cos(y)


def df_dx(x, y):
    return -np.sin(x) * np.cos(y)


def df_dy(x, y):
    return -np.cos(x) * np.sin(y)


x = np.linspace(-2 * np.pi, 2 * np.pi, 100)
y = np.linspace(-2 * np.pi, 2 * np.pi, 100)

X, Y = np.meshgrid(x, y)  #

Z = f(X, Y)

fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(1, 1, 1, projection="3d")  #

surf = ax.plot_surface(X, Y, Z, cmap="viridis", edgecolor="none")
fig.colorbar(surf)
ax.set_title(f"Superfície f(x,y)")
plt.show()


fig2 = plt.figure(figsize=(8, 6))
ax2 = fig2.add_subplot(1, 1, 1)
mapa = ax2.contourf(X, Y, Z, cmap="rainbow", edgecolor="none")
fig2.colorbar(mapa)
ax2.set_title(f"Curvas de nível de f(x,y)")
plt.show()


U = df_dx(X, Y)
V = df_dy(X, Y)

fig3 = plt.figure(figsize=(8, 6))
ax3 = fig3.add_subplot(1, 1, 1)

ax3.contourf(X, Y, Z, levels=15, cmap="viridis", alpha=0.6)
ax3.set_xlim(-3, 3)
ax3.set_ylim(-3, 3)
ax3.quiver(X, Y, U, V, color="red")
ax3.set_title("Gradiente de f(x,y)")
plt.show()
