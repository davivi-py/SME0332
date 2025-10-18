import numpy as np 
import matplotlib.pyplot as plt

def rand_walk(N):

    x0 = np.zeros(N+1)
    y0 = np.zeros(N+1)

    sorteador = np.random.randint(0, 4, N+1)
    delta = 1

    for i in range(1,N+1):
        x0[i] = x0[i-1]
        y0[i] = y0[i-1]


        if sorteador[i] == 0:
            x0[i] += delta
        elif sorteador[i] == 1:
            x0[i] += -delta
        elif sorteador[i] == 2:
            y0[i] += delta
        else:
            y0[i] += -delta 

    plt.plot(x0, y0)  
    plt.title(f'Caminhada aleatória 2D com {N} passos')  
    plt.xlabel('x')  
    plt.ylabel('y')  
    plt.grid(True)  
    plt.show()

    return x,y

def dqm(M, N):

    msd = np.zeros(N+1)

    for _ in range(M):
        x, y = rand_walk(N)
        dx = x - x[0]
        dy = y - y[0]

        sdq += dx**2 + dy**2 
    
    msd /= M
    return msd

M = 1000
N = 10000

msd = dqm(M, N)

plt.figure(figsize=(8,6))
plt.plot(range(N+1), msd, label='MSD (distância quadrática média)')
plt.xlabel('Passos (t)')
plt.ylabel(r'$d_m^2(t)$')
plt.title('Distância Quadrática Média para Caminhada Aleatória 2D')
plt.grid(True)
plt.legend()
plt.show()