import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
import random

caminho = r"C:\Users\User\Desktop\SME0332\TOPICOS VARIADOS DE PYTHON\Processamento de imagens\stinkbug.png"

img = mpimg.imread(caminho)

if len(img.shape) > 2:  # aqui a gente garante que a imagem é 2D
    img_cinza = img[:, :, 0]
else:
    img_cinza = img


def manchador(img, num_manchas=20):

    img_new = np.copy(img)

    h, w = img_new.shape

    for i in range(num_manchas):
        cx = random.randint(0, w)
        cy = random.randint(0, h)
        raio = random.randint(5, 20)
        cor = random.choice([0.0, 1.0])

        y_min = max(0, cy - raio)
        y_max = min(h, cy + raio)
        x_min = max(0, cx - raio)
        x_max = min(w, cx + raio)

        for y in range(y_min, y_max):
            for x in range(x_min, x_max):
                distancia_sq = (x - cx) ** 2 + (y - cy) ** 2

                if distancia_sq <= raio**2:
                    img_new[y, x] = cor
    return img_new


dirty_work = manchador(img_cinza, num_manchas=30)

plt.imshow(dirty_work, cmap="gray")
plt.title("Stinkbug sujo de bolinhas")
plt.show()
