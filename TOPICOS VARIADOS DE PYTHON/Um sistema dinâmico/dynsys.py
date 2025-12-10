import numpy as np 
import matplotlib.pyplot as plt

def verlet_velocidade(m2):
    gamma = 1.0
    dt = 0.01
    m1 = 1.0
    steps = 2000

    r1 = np.array([0.0,0.0])
    v1 = np.array([0.0,0.0])

    r2 = np.array([1.0,0.0])
    v2 = np.array([0.0,1.0])

    historico = np.zeros((steps, 9))

    tn = 0.0
    n = 0

    while n < steps:
        r12 = r2 - r1
        dist = np.linalg.norm(r12)
        F = gamma * m2 * m1 / dist**3

        a1 = F * r12 / m1
        a2 = -F * r12 / m2

        r1_new = r1 + v1*dt + 0.5*a1*(dt)**2
        r2_new = r2 + v2*dt + 0.5*a2*(dt)**2

        r12_new = r2_new - r1_new 
        dist_new = np.linalg.norm(r12_new)
        F_new = gamma*m1*m2 / dist_new**3

        a1_new = F_new * r12_new / m1
        a2_new = -F_new * r12_new / m2

        v1_new =  v1 + 0.5*(a1+a1_new)*dt
        v2_new = v2 + 0.5*(a2+a2_new)*dt

        historico[n] = [tn, r1[0], r1[1], v1[0], v1[1], r2[0], r2[1], v2[0], v2[1]]

        tn = tn + dt

        n = n + 1

        r1 = r1_new
        r2 = r2_new

        v1 = v1_new
        v2 = v2_new

    return historico      

def sim_n_save(m2, filename='evol.txt'):

    historico = verlet_velocidade(m2)

    np.savetxt(filename, historico, fmt='%.8f')

def load_n_plot(m2, filename='evol.txt'):

    dados = np.loadtxt(filename)

    t = dados[:, 0]

    r1x = dados[:, 1]
    r1y = dados[:, 2]
    v1x = dados[:, 3]
    v1y = dados[:, 4]
    r2x = dados[:, 5]
    r2y = dados[:, 6]
    v2x = dados[:, 7]
    v2y = dados[:, 8]

    m1 = 1.0

    norm_v1 = v1x**2 + v1y**2
    norm_v2 = v2x**2 + v2y**2

    K = 0.5*m1*norm_v1+0.5*m2*norm_v2

    plt.figure(figsize=(16,10))

    plt.subplot(1,2,1)
    plt.plot(r1x,r1y, label='Corpo 1')
    plt.plot(r2x,r2y, label='Corpo 2')
    plt.title('Trajetória dos Corpos m2={m2}')
    plt.xlabel('Eixo X')
    plt.ylabel('Eixo Y')
    plt.legend()
    plt.grid(True)
    plt.axis('equal')

    plt.subplot(1,2,2)
    plt.plot(t,K, label='Energia Cinética em função do tempo')
    plt.title('Energia Cinética Total do Sistema')
    plt.xlabel('Tempo(t)')
    plt.ylabel('Energia Cinética(t)')
    plt.grid(True)
    plt.tight_layout()
    plt.show()


def magica():

    lista_massas = [0.001, 0.01, 0.1, 1.0, 2.0]

    for m in lista_massas:

        nome_arq = "simulacao_m2_{m}"

        sim_n_save(m,nome_arq)

        load_n_plot(m, nome_arq)

magica()