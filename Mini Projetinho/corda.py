import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad

L = 1.0

tau = 2.0

g = 9.81

def rho_1(x):
    return 1.0

def rho_2(x):
    return 0.5*(1+np.exp(-100*(x-0.5)**2))

def calc_masses(N, rho_func):

    l0 = L / N

    massas = np.zeros(N+1)

    m0, _ = quad(rho_func,0,0.5*l0)

    mf, _ = quad(rho_func,(L-0.5*l0), L)

    massas[0] = m0

    massas[N-1] = mf

    for i in range(1,N-1):
        lower_limit = (i-0.5)*l0
        upper_limit = (i+0.5)*l0
        massas[i], _ = quad(rho_func, lower_limit, upper_limit)

    return massas

def jacobi_solver(massas, num_it):

    N = len(massas)-1

    l0 = L / N

    tol = 10**(-7)

    y_old = np.zeros(N+1)
    y_new = np.zeros(N+1)

    for k in range(num_it):
        for i in range(1, N):

            y_new[i] = 0.5*(y_old[i-1]+y_old[i+1])-(l0*massas[i]*g / (2*tau))

        y_old = y_new.copy()
    erro = np.max(np.abs(y_new-y_old))
    if erro < tol:
        return y_new


    return y_new

def gauss_solver(massas, num_it):

    N = len(massas)-1

    l0 = L / N

    tol = 10**(-7)

    y = np.zeros(N+1)

    for k in range(num_it):
        y_old = y.copy()
        for i in range(1,N):
            y[i] = 0.5*(y[i-1]+y[i+1]) - (l0*massas[i]*g / 2*tau)

        erro = np.max(np.abs(y-y_old))

        if erro < tol:
            return y
    return y

plt.figure(figsize=(14,10))

Ns = [10,20,40,80]
plt.subplot(2,2,1)

for N in Ns:

    massas = calc_masses(N, rho_1)
    y = jacobi_solver(massas, 5000)

    x = np.linspace(0,L,N+1)
    plt.plot(x,y, label=f"N={N}")

plt.title('Rho constante(Jacobi)')
plt.xlabel('Eixo X')
plt.ylabel('Eixo Y')
plt.grid(True)
plt.legend()

plt.subplot(2,2,2)

for N in Ns:

    massas = calc_masses(N, rho_2)
    y = jacobi_solver(massas, 5000)

    x = np.linspace(0,L,N+1)
    plt.plot(x,y, label=f'N={N}')

plt.title('Rho variável(Jacobi)')
plt.xlabel('Eixo X')
plt.ylabel('Eixo Y')
plt.grid(True)
plt.legend()

plt.subplot(2,2,3)

for N in Ns:

    massas = calc_masses(N, rho_1)
    y = gauss_solver(massas, 5000)

    x = np.linspace(0,L,N+1)
    plt.plot(x,y, label=f'N={N}')

plt.title('Rho constante(Gauss-Siedel)')
plt.xlabel('Eixo X')
plt.ylabel('Eixo Y')
plt.grid(True)
plt.legend()

plt.subplot(2,2,4)

for N in Ns:

    massas = calc_masses(N, rho_2)
    y = gauss_solver(massas, 5000)

    x = np.linspace(0,L,N+1)
    plt.plot(x,y, label=f'N={N}')

plt.title('Rho variável(Gauss-Siedel)')
plt.xlabel('Eixo X')
plt.ylabel('Eixo Y')
plt.grid(True)
plt.legend()
plt.show()


