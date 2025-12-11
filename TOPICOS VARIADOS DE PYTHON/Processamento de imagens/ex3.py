import matplotlib.pyplot as plt
import numpy as np


def suaviza_cruz(matriz):

    linhas, cols = matriz.shape
    matriz_new = matriz.copy()

    for i in range(1, linhas - 1):
        for j in range(1, cols - 1):

            soma = (
                matriz[i, j]
                + matriz[i - 1, j]
                + matriz[i + 1, j]
                + matriz[i, j - 1]
                + matriz[i, j + 1]
            )

            matriz_new[i, j] = soma / 5.0

    return matriz_new

def suaviza_3x3(matriz):

    linhas,cols = matriz.shape
    matriz_new = matriz.copy()

    for i in range(1, linhas-1):
        for j in range(1, cols-1):

            soma = (
                matriz[i,j]
                + matriz[i - 1, j]
                + matriz[i + 1, j]
                + matriz[i, j - 1]
                + matriz[i, j + 1]
                + matriz[i-1, j-1]
                + matriz[i-1, j+1]
                + matriz[i+1, j-1]
                + matriz[i+1, j+1]
            )

            matriz_new[i, j] = soma / 9.0


    return matriz_new


img_aleatória = np.zeros((100,100))
img_aleatória[30:70, 30:70] = 1.0
img_aleatória += np.random.normal(0, 0.1, (100,100))

img_cruz = img_aleatória.copy()

n = 8

for _ in range(n+1):
    img_cruz = suaviza_cruz(img_cruz)

img_3x3 = img_aleatória.copy()
for _ in range(n+1):
    img_3x3 = suaviza_3x3(img_3x3)


plt.figure(figsize=(10,8))

plt.subplot(2,2,1)
plt.imshow(img_aleatória, cmap="gray")
plt.title('Imagem Original')
plt.axis("off")

plt.subplot(2,2,2)
plt.imshow(img_cruz, cmap="gray")
plt.title('Suavização em cruz')
plt.axis('off')

plt.subplot(2,2,4)
plt.imshow(img_3x3, cmap='gray')
plt.title('Método 3x3')
plt.axis('off')

plt.tight_layout(pad=3.0)
plt.show()