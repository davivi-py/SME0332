import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.colors import ListedColormap


def init_sim(n, k):

    grid = np.zeros((n, n))

    for _ in range(k):

        x = np.random.randint(0, n)
        y = np.random.randint(0, n)

        grid[x, y] = 2

    center = n // 2
    grid[center, center] = 1

    return grid


def update(grid):

    n = grid.shape[0]

    grid_new = grid.copy()

    for i in range(n):
        for j in range(n):

            if grid[i, j] == 1:
                    # dir
                if j < n - 1 and grid[i, j + 1] == 0:
                    grid_new[i, j + 1] = 1
                    # esq
                if j > 0 and grid[i, j - 1] == 0:
                    grid_new[i, j - 1] = 1
                    # baixo
                if i < n - 1 and grid[i + 1, j] == 0:
                    grid_new[i + 1, j] = 1
                    # cima
                if i > 0 and grid[i - 1, j] == 0:
                    grid_new[i - 1, j] = 1

    return grid_new


N = 50
Obstaculos = 400
grid = init_sim(N, Obstaculos)

cmap = ListedColormap(["white", "deepskyblue", "black"])

fig, ax = plt.subplots(figsize=(6, 6))
ax.set_title("Flooding Simulation")


img = ax.imshow(grid, cmap=cmap)


def animate(frame):

    global grid

    grid = update(grid)

    img.set_data(grid)
    return [img]


ani = FuncAnimation(fig, animate, frames=200, interval=50, blit=True)
plt.grid(True)
plt.show()
