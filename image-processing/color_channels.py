import matplotlib.pyplot as plt
import matplotlib.image as mpimg

caminho = r"C:\Users\User\Desktop\SME0332\TOPICOS VARIADOS DE PYTHON\Processamento de imagens\stinkbug.png"

img = mpimg.imread(caminho)

canal_A = img[:, :, 0]

plt.figure()
plt.imshow(canal_A, cmap='hot')
plt.title("Mapa de cor HOT")
plt.colorbar()
plt.show()

plt.figure()
plt.imshow(canal_A, cmap="nipy_spectral")
plt.title("Mapa de cor Nipy Spectral")
plt.colorbar()
plt.show()
