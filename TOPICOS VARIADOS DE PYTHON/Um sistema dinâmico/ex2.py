import numpy as np


gamma = 1.0
dt = 0.01
m1 = 1.0
m2 = 1.0
N_steps = 2000

r1 = np.array([0.0, 0.0])
v1 = np.array([0.0, 0.0])
r2 = np.array([1.0, 0.0])
v2 = np.array([0.0, 1.0])

solution = np.zeros((N_steps, 9))

tn = 0.0
n = 0

while n < N_steps:
    r12 = r2 - r1
    dist = np.linalg.norm(r12)
    
    F = gamma * m1 * m2 / dist**3
    F1 = F * r12
    F2 = -F1
    
    a1 = F1 / m1
    a2 = F2 / m2
    
    r1_new = r1 + v1 * dt + 0.5 * a1 * dt**2
    r2_new = r2 + v2 * dt + 0.5 * a2 * dt**2
    
    r12_new = r2_new - r1_new
    dist_new = np.linalg.norm(r12_new)
    F_new = gamma * m1 * m2 / dist_new**3
    F1_new = F_new * r12_new
    F2_new = -F1_new
    
    a1_new = F1_new / m1
    a2_new = F2_new / m2
    
    v1_new = v1 + 0.5 * (a1 + a1_new) * dt
    v2_new = v2 + 0.5 * (a2 + a2_new) * dt
    
    solution[n, :] = tn, r1[0], r1[1], v1[0], v1[1], r2[0], r2[1], v2[0], v2[1]
    
    r1 = r1_new
    v1 = v1_new
    r2 = r2_new
    v2 = v2_new
    tn = tn + dt
    n = n + 1

np.savetxt('evol.txt', solution)
print("Arquivo evol.txt salvo")