import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad

g = 9.81
L = 1.0
tau = 2.0
N = 80  # muda aqui pra testar outros valores

def densidade1(x):
    return 1.0

def densidade2(x):
    return 0.5 * (1 + np.exp(-100 * (x - 0.5)**2))

def diametro(x):
    return 2 * (1 + np.exp(-200 * (x - 0.5)**2))

def calc_massas(func_dens, N):
    l0 = L / N
    m = np.zeros(N + 1)
    m[0], _ = quad(func_dens, 0, 0.5 * l0)
    for i in range(1, N):
        m[i], _ = quad(func_dens, (i - 0.5) * l0, (i + 0.5) * l0)
    m[N], _ = quad(func_dens, (N - 0.5) * l0, L)
    return m

def jacobi(m, f_ext, N):
    l0 = L / N
    y = np.zeros(N + 1)
    y_new = np.zeros(N + 1)
    
    for k in range(5000):
        for i in range(1, N):
            if i in f_ext:
                f = f_ext[i]
            else:
                f = 0.0
            y_new[i] = (y[i-1] + y[i+1]) / 2 + (l0 / (2 * tau)) * (-m[i]*g + f)
        if np.linalg.norm(y_new - y) < 1e-7:
            break
        for i in range(N+1):
            y[i] = y_new[i]
    return y_new

def gauss_seidel(m, f_ext, N):
    l0 = L / N
    y = np.zeros(N + 1)
    
    for k in range(5000):
        y_old = np.zeros(N + 1)
        for i in range(N+1):
            y_old[i] = y[i]
        for i in range(1, N):
            if i in f_ext:
                f = f_ext[i]
            else:
                f = 0.0
            y[i] = (y[i-1] + y[i+1]) / 2 + (l0 / (2 * tau)) * (-m[i]*g + f)
        if np.linalg.norm(y - y_old) < 1e-7:
            break
    return y

# item 1
m1 = calc_massas(densidade1, N)
m2 = calc_massas(densidade2, N)
print(f"N={N}: rho1={np.sum(m1):.4f} kg, rho2={np.sum(m2):.4f} kg")

# figura unica
plt.figure(figsize=(12, 6))

# itens 2 e 3
x = np.linspace(0, L, N + 1)
y_j1 = jacobi(m1, {}, N)
y_g1 = gauss_seidel(m1, {}, N)
y_j2 = jacobi(m2, {}, N)
y_g2 = gauss_seidel(m2, {}, N)

plt.subplot(2, 3, 1)
plt.plot(x, y_j1, 'b-', label='Jacobi')
plt.plot(x, y_g1, 'r--', label='Gauss-Seidel')
plt.title(f'N={N}, rho=1')
plt.grid(True)
plt.legend()

plt.subplot(2, 3, 2)
plt.plot(x, y_j2, 'b-', label='Jacobi')
plt.plot(x, y_g2, 'r--', label='Gauss-Seidel')
plt.title(f'N={N}, rho variavel')
plt.grid(True)
plt.legend()

# item 4
forcas = np.linspace(0, -50, 30)
deslocamentos = []
for f in forcas:
    y = jacobi(m1, {39: f}, N)
    deslocamentos.append(y[39])

plt.subplot(2, 3, 3)
plt.plot(forcas, deslocamentos, 'o-')
plt.xlabel('Forca f(39)')
plt.ylabel('y[39]')
plt.grid(True)
plt.title('Item 4: Forca variavel')

# item 5
y_opostas = gauss_seidel(m1, {17: 20, 30: -15}, N)
y_ref = gauss_seidel(m1, {}, N)

plt.subplot(2, 3, 4)
plt.plot(x, y_opostas, 'g-', linewidth=2)
plt.plot(x, y_ref, 'k--', alpha=0.5)
plt.scatter([x[17], x[30]], [y_opostas[17], y_opostas[30]], color='red', s=80)
plt.grid(True)
plt.title('Item 5: Forcas opostas')

# item 6
l0 = L / N
rho_f = 1000
rho_c = 900

y = np.zeros(N + 1)
for k in range(5000):
    y_old = np.zeros(N + 1)
    for i in range(N+1):
        y_old[i] = y[i]
    for i in range(1, N):
        V, _ = quad(lambda xi: np.pi * (diametro(xi)/2)**2, (i-0.5)*l0, (i+0.5)*l0)
        m = rho_c * V
        F_emp = rho_f * V * g
        y[i] = (y[i-1] + y[i+1]) / 2 + (l0 / (2*tau)) * (-m*g + F_emp)
    if np.linalg.norm(y - y_old) < 1e-7:
        break

y_sem = np.zeros(N + 1)
for k in range(5000):
    y_old = np.zeros(N + 1)
    for i in range(N+1):
        y_old[i] = y_sem[i]
    for i in range(1, N):
        V, _ = quad(lambda xi: np.pi * (diametro(xi)/2)**2, (i-0.5)*l0, (i+0.5)*l0)
        m = rho_c * V
        y_sem[i] = (y_sem[i-1] + y_sem[i+1]) / 2 + (l0 / (2*tau)) * (-m*g)
    if np.linalg.norm(y_sem - y_old) < 1e-7:
        break

plt.subplot(2, 3, 5)
plt.plot(x, y, 'b-', linewidth=2, label='com empuxo')
plt.plot(x, y_sem, 'r--', label='sem empuxo')
plt.legend()
plt.grid(True)
plt.title('Item 6: Empuxo')

plt.tight_layout()
plt.show()