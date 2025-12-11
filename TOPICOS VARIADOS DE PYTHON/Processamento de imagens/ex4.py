import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np

path = r"C:\Users\User\Desktop\SME0332\TOPICOS VARIADOS DE PYTHON\Processamento de imagens\concrete.jpg"
img = mpimg.imread(path)

taman = img.shape

print(taman)

A = img[:, :, 0]

crop = A[38:353, 113:443]

normalizada = crop / 255.0

limiar = 0.35

img_bin = (normalizada < limiar)

num_agregados = np.sum(img_bin)

fracao_agreg = num_agregados / img_bin.size

print(f'A fração de agregados na imagem é de: {fracao_agreg}')

plt.imshow(crop, cmap="gray")
plt.show()
