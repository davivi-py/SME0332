import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np


def suaviza_cruz(A):
    m, n = A.shape
    B = np.zeros_like(A)

    for i in range(m):
        for j in range(n):
            soma = A[i, j]
            count = 1

            if i > 0:
                soma += A[i-1, j]
                count += 1
            if i < m - 1:
                soma += A[i+1, j]
                count += 1
            if j > 0:
                soma += A[i, j-1]
                count += 1
            if j < n - 1:
                soma += A[i, j+1]
                count += 1

            B[i, j] = soma / count

    return B


def suaviza_completo(A):
    m, n = A.shape
    B = np.zeros_like(A)

    for i in range(m):
        for j in range(n):
            soma = 0.0
            count = 0

            for di in [-1, 0, 1]:
                for dj in [-1, 0, 1]:
                    ni, nj = i + di, j + dj
                    if 0 <= ni < m and 0 <= nj < n:
                        soma += A[ni, nj]
                        count += 1

            B[i, j] = soma / count

    return B


def main():
    img = mpimg.imread('stinkbug.png')
    A = img[:, :, 0]

    num_aplicacoes = 5
    resultados_cruz = [A]
    resultados_completo = [A]

    temp_cruz = A.copy()
    temp_completo = A.copy()

    for _ in range(num_aplicacoes):
        temp_cruz = suaviza_cruz(temp_cruz)
        resultados_cruz.append(temp_cruz.copy())

        temp_completo = suaviza_completo(temp_completo)
        resultados_completo.append(temp_completo.copy())

    fig, axes = plt.subplots(2, num_aplicacoes + 1, figsize=(15, 6))

    for idx, img_res in enumerate(resultados_cruz):
        axes[0, idx].imshow(img_res, cmap='gray')
        axes[0, idx].set_title(f'Cruz - {idx}x')
        axes[0, idx].axis('off')

    for idx, img_res in enumerate(resultados_completo):
        axes[1, idx].imshow(img_res, cmap='gray')
        axes[1, idx].set_title(f'Completo - {idx}x')
        axes[1, idx].axis('off')

    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()