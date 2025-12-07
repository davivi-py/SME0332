import matplotlib.pyplot as plt
import matplotlib.image as mpimg


def main():
    img = mpimg.imread('stinkbug.png')
    A = img[:, :, 0]

    fig, axes = plt.subplots(1, 4, figsize=(16, 4))

    axes[0].imshow(img)
    axes[0].set_title('Imagem original (RGB)')
    axes[0].axis('off')

    axes[1].imshow(A, cmap='gray')
    axes[1].set_title('Canal A (gray)')
    axes[1].axis('off')

    axes[2].imshow(A, cmap='hot')
    axes[2].set_title('Canal A (hot)')
    axes[2].axis('off')

    axes[3].imshow(A, cmap='nipy_spectral')
    axes[3].set_title('Canal A (nipy_spectral)')
    axes[3].axis('off')

    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()