import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

N = 50

grade = np.zeros((N, N))

centro = N // 2
grade[centro, centro] = 1

num_obstaculos = 100
for i in range(num_obstaculos):
    x = np.random.randint(0, N)
    y = np.random.randint(0, N)
    grade[x, y] = 2

grade[centro, centro] = 1


def update(frame):
    global grade
    
    nova_grade = grade.copy()
    
    for i in range(N):
        for j in range(N):
            if grade[i, j] == 1:
                if i > 0 and grade[i-1, j] == 0:
                    nova_grade[i-1, j] = 1
                if i < N-1 and grade[i+1, j] == 0:
                    nova_grade[i+1, j] = 1
                if j > 0 and grade[i, j-1] == 0:
                    nova_grade[i, j-1] = 1
                if j < N-1 and grade[i, j+1] == 0:
                    nova_grade[i, j+1] = 1
    
    grade = nova_grade
    
    img.set_data(grade)
    return [img]


fig, ax = plt.subplots(figsize=(8, 8))
img = ax.imshow(grade, cmap='Blues', vmin=0, vmax=2)
ax.set_title('Algoritmo de Flooding')
ax.axis('off')

anim = FuncAnimation(fig, update, frames=200, interval=50, blit=True)

plt.show()