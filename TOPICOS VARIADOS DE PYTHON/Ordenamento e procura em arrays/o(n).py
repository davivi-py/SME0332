import numpy as np
import matplotlib.pyplot as plt
import time


def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr


def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr


def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)


tamanhos = [100, 200, 400, 800, 1600]

tempo_bubble = []
tempo_selection = []
tempo_quick = []

for N in tamanhos:
    print(f"Testando N = {N}")
    
    arr = np.random.randint(0, 1000, N).tolist()
    
    arr_copia = arr.copy()
    inicio = time.time()
    bubble_sort(arr_copia)
    fim = time.time()
    tempo_bubble.append(fim - inicio)
    
    arr_copia = arr.copy()
    inicio = time.time()
    selection_sort(arr_copia)
    fim = time.time()
    tempo_selection.append(fim - inicio)
    
    arr_copia = arr.copy()
    inicio = time.time()
    quick_sort(arr_copia)
    fim = time.time()
    tempo_quick.append(fim - inicio)

plt.figure(figsize=(10, 6))
plt.loglog(tamanhos, tempo_bubble, 'o-', label='Bubble Sort', linewidth=2)
plt.loglog(tamanhos, tempo_selection, 's-', label='Selection Sort', linewidth=2)
plt.loglog(tamanhos, tempo_quick, '^-', label='Quick Sort', linewidth=2)
plt.xlabel('Tamanho do array (N)')
plt.ylabel('Tempo (segundos)')
plt.title('Comparação de Algoritmos de Ordenamento')
plt.legend()
plt.grid(True, alpha=0.3)
plt.show()

print("\n--- RESULTADOS ---")
for i, N in enumerate(tamanhos):
    print(f"N = {N}")
    print(f"  Bubble:    {tempo_bubble[i]:.6f} s")
    print(f"  Selection: {tempo_selection[i]:.6f} s")
    print(f"  Quick:     {tempo_quick[i]:.6f} s")