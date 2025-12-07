import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np


def adicionar_manchas(A, num_manchas=10, raio=20):
    B = A.copy()
    altura, largura = B.shape

    for _ in range(num_manchas):
        cx = np.random.randint(raio, largura - raio)
        cy = np.random.randint(raio, altura - raio)
        cor = np.random.choice([0.0, 1.0])

        for i in range(cy - raio, cy + raio):
            for j in range(cx - raio, cx + raio):
                if (i - cy)**2 + (j - cx)**2 <= raio**2:
                    B[i, j] = cor

    return B


def main():
    img = mpimg.imread('stinkbug.png')
    A = img[:, :, 0]

    B = adicionar_manchas(A, num_manchas=15, raio=25)

    fig, axes = plt.subplots(1, 2, figsize=(10, 5))

    axes[0].imshow(A, cmap='gray')
    axes[0].set_title('Original')
    axes[0].axis('off')

    axes[1].imshow(B, cmap='gray')
    axes[1].set_title('Com manchas')
    axes[1].axis('off')

    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()