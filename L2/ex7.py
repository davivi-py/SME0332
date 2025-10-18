import numpy as np 

def moeda_launcher(N):

    jogadas = np.random.randint(0, 2, N)

    contagem_rep = 0

    i = 0

    while i <= N - 3:

        if jogadas[i] == 1 and jogadas[i+1] and jogadas [i+2] == 1:
            contagem_rep += 1
            i += 3
        else:

            i += 1
    prob = contagem_rep / N
    print(prob)

moeda_launcher(1000000)