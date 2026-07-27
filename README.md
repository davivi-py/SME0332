# SME0332 — Computação Científica com Python

Projetos e exercícios da disciplina **SME0332** (ICMC-USP), cobrindo métodos numéricos, simulações, algoritmos e processamento de imagens em Python.

**Stack:** Python · NumPy · Matplotlib · SciPy

---

## Estrutura

```
├── numerical-methods/    # Solvers iterativos, Monte Carlo, integração
├── simulations/          # Simulações de sistemas físicos
├── algorithms/           # Benchmarks de ordenação, visualização de funções
└── image-processing/     # Filtros, segmentação, ruído
```

---

## Destaques

### 🔵 Simulação de N-corpos — Integrador Velocity Verlet

[`simulations/nbody_simulation.py`](simulations/nbody_simulation.py)

Simula um sistema gravitacional de dois corpos usando o algoritmo Velocity Verlet. Rastreia posição e velocidade ao longo do tempo, salva os dados da simulação em arquivo, e plota as trajetórias orbitais junto com a evolução da energia cinética total. Testado em cinco proporções de massa diferentes.

### 🔵 Corda sob gravidade — Solvers de Jacobi e Gauss-Seidel

[`simulations/rope_simulation.py`](simulations/rope_simulation.py)

Modela a forma de equilíbrio de uma corda com densidade linear variável sob gravidade. Resolve o sistema tridiagonal resultante usando os métodos iterativos de Jacobi e Gauss-Seidel, comparando a convergência entre diferentes refinamentos de grade (N = 10, 20, 40, 80).

### 🔵 Animação de Flood Fill

[`simulations/flood_fill.py`](simulations/flood_fill.py)

Flood fill animado (estilo BFS) em uma grade 2D com obstáculos posicionados aleatoriamente. Construído com `matplotlib.animation.FuncAnimation`.

### 🔵 Métodos de Monte Carlo

[`numerical-methods/monte_carlo_area.py`](numerical-methods/monte_carlo_area.py) · [`numerical-methods/monte_carlo_3d.py`](numerical-methods/monte_carlo_3d.py)

Estimativa de área entre duas curvas usando amostragem Monte Carlo. A variante 3D estima π amostrando pontos dentro de uma esfera unitária.

### 🔵 Benchmark de Algoritmos de Ordenação

[`algorithms/sorting_benchmark.py`](algorithms/sorting_benchmark.py)

Comparação empírica de tempo de execução entre Bubble Sort, Selection Sort e Quick Sort, para tamanhos de array entre 100 e 1600. Resultados plotados em escala log-log para confirmar a complexidade O(n²) vs O(n log n).

### 🔵 Solver Iterativo de Jacobi

[`numerical-methods/jacobi_general.py`](numerical-methods/jacobi_general.py)

Solver de Jacobi genérico n×n para sistemas lineares diagonalmente dominantes. Uma implementação separada 2×2 rastreia a taxa de convergência em função da tolerância (ε de 10⁻² a 10⁻⁸).

### 🔵 Processamento de Imagens

[`image-processing/`](image-processing/)

Implementação manual de filtros de suavização com kernel em cruz e 3×3. Segmentação binária via limiarização para detecção de fração de agregados em imagens em tons de cinza.

---

## Executando

```
pip install numpy matplotlib scipy
python simulations/nbody_simulation.py
```

Cada script é independente e pode ser executado separadamente.

---

*Repositório desenvolvido durante a disciplina SME0332 (Fundamentos de Programação de Computadores com Aplicações em Python para Física e Bioinformática), ICMC-USP, 2025.*
