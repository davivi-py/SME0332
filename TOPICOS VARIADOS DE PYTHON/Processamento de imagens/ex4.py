import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np


def main():
    img = mpimg.imread('concrete.jpg')
    A = img[:, :, 0]

    print(f"Dimensões da imagem: {A.shape}")

    y_inicio, y_fim = 50, 300
    x_inicio, x_fim = 50, 300
    recortada = A[y_inicio:y_fim, x_inicio:x_fim]

    A_norm = recortada / recortada.max()

    limiares = [0.3, 0.4, 0.5, 0.6, 0.7]

    fig, axes = plt.subplots(2, len(limiares), figsize=(15, 6))

    for idx, limiar in enumerate(limiares):
        img_bin = (A_norm < limiar) * 1.0
        fracao = np.mean(img_bin)

        axes[0, idx].imshow(A_norm, cmap='gray')
        axes[0, idx].set_title(f'Original recortada')
        axes[0, idx].axis('off')

        axes[1, idx].imshow(img_bin, cmap='gray')
        axes[1, idx].set_title(f'Limiar={limiar}\nFração={fracao:.3f}')
        axes[1, idx].axis('off')

    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()