import numpy as np
import time
#calculando a soma de rellman
#precisa integrar qualquer função
def somaRNaoVetorizada(N, a, b,f):
    dx = (b-a)/N
    #N tem diferentes valores

    for i in range(N):
        x = (a+(i+1)+dx)
        soma += f(x)

        return soma+dx
    
    def minhafunc(x):
        return np.sqrt(np.maximum(0.0, 1.0 - x**2))
    N = 10000
    a = 0.0
    b = 1.0
    ti = time.time()
    minhasoma = somaRNaoVetorizada(N, a, b, minhafunc)
    print('tempo total= ', time.time()-ti)
    print(4*minhasoma)

#soma de R vetorizada
def minhafunc(x):
        return np.sqrt(np.maximum(0.0, 1.0 - x**2))
def somaRVetorizada(N,a,b,f):
  #intervalo definico por a e b onde N soma mais 1
    dx = (b-a)/N
    x = np.linspace(a,b,N+1)
    return np.sum(f(x[1:]+ dx))
#acomulação do erro de arredondamento

N = 10000
a = 0.0
b = 1.0
ti = time.time()
minhasoma = somaRVetorizada(N, a, b, minhafunc)
print('tempo total= ', time.time()-ti)
print(4*minhasoma,np.pi)