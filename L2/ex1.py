import numpy as np
import matplotlib.pyplot as plt

def jogador_dados(M,N):

    jogadas = np.random.randint(low=1, high=7, size=(N,M))

    soma = np.sum(jogadas, axis=1)

    counts, bins = np.histogram(soma)
    plt.stairs(counts, bins)
    plt.show()

jogador_dados(100000,1000)






