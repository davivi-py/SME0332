"""
Flood Fill Simulation
=====================
Animated BFS-style flood fill on a 2D grid with randomly placed obstacles.
The flood originates from the center and expands outward, blocked by obstacles.

Usage:
    python flood_fill.py
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.colors import ListedColormap

GRID_SIZE = 50
NUM_OBSTACLES = 400


def init_grid(n, num_obstacles):
    """Initialize grid with random obstacles (2) and a flood source at center (1)."""
    grid = np.zeros((n, n))
    for _ in range(num_obstacles):
        x, y = np.random.randint(0, n, size=2)
        grid[x, y] = 2
    center = n // 2
    grid[center, center] = 1
    return grid


def step(grid):
    """Expand flood by one step in four directions, blocked by obstacles."""
    n = grid.shape[0]
    grid_new = grid.copy()
    for i in range(n):
        for j in range(n):
            if grid[i, j] == 1:
                for di, dj in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    ni, nj = i + di, j + dj
                    if 0 <= ni < n and 0 <= nj < n and grid[ni, nj] == 0:
                        grid_new[ni, nj] = 1
    return grid_new


grid = init_grid(GRID_SIZE, NUM_OBSTACLES)
cmap = ListedColormap(["white", "deepskyblue", "black"])

fig, ax = plt.subplots(figsize=(6, 6))
ax.set_title("Flood Fill Simulation")
img = ax.imshow(grid, cmap=cmap)


def animate(frame):
    global grid
    grid = step(grid)
    img.set_data(grid)
    return [img]


ani = FuncAnimation(fig, animate, frames=200, interval=50, blit=True)
plt.show()
