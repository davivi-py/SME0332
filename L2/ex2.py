import numpy as np
import matplotlib.pyplot as plt

def calc_pi(N):
    
    x = np.random.uniform(-1, 1, N)
    y = np.random.uniform(-1, 1, N)
    
    count_in = np.sum(x**2+y**2 < 1.0)
    return 4 * count_in / N

def calc_pi_it(N, R):
  resultados = []
  erros = []
  for i in range(1, R+1):
    resultados.append(calc_pi(N))
    pi_med = np.mean(resultados)
    erros.append(abs(np.pi - pi_med))

  plt.figure(figsize=(10,8))
  plt.grid(True)
  plt.loglog(range(1, R+1), erros, linewidth='3',linestyle='--', label='Erro de π em função do número N de realizações do teste')
  plt.xlabel('Número de iterações')
  plt.ylabel('|π - π(médio)|')
  plt.show()

  return (resultados, pi_med)

calc_pi_it(10000000, 10)
  
  

  






















    

    


    

    

    




