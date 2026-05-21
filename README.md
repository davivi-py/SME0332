# SME0332 — Scientific Computing with Python

Projects and exercises from the **SME0332** course at ICMC-USP, covering numerical methods, simulations, algorithms, and image processing using Python.

**Stack:** Python · NumPy · Matplotlib · SciPy

---

## Structure

```
├── numerical-methods/    # Iterative solvers, Monte Carlo, integration
├── simulations/          # Physical system simulations
├── algorithms/           # Sorting benchmarks, function visualization
└── image-processing/     # Filters, segmentation, noise
```

---

## Highlights

### 🔵 N-Body Simulation — Velocity Verlet integrator
[`simulations/nbody_simulation.py`](simulations/nbody_simulation.py)

Simulates a two-body gravitational system using the Velocity Verlet algorithm. Tracks position and velocity over time, saves simulation data to file, and plots orbital trajectories alongside total kinetic energy evolution. Tested across five different mass ratios.

### 🔵 Rope Under Gravity — Jacobi & Gauss-Seidel solvers
[`simulations/rope_simulation.py`](simulations/rope_simulation.py)

Models the equilibrium shape of a rope with variable linear density under gravity. Solves the resulting tridiagonal system using both Jacobi and Gauss-Seidel iterative methods, comparing convergence across grid refinements (N = 10, 20, 40, 80).

### 🔵 Flood Fill Animation
[`simulations/flood_fill.py`](simulations/flood_fill.py)

Animated BFS-style flood fill on a 2D grid with randomly placed obstacles. Built with `matplotlib.animation.FuncAnimation`.

### 🔵 Monte Carlo Methods
[`numerical-methods/monte_carlo_area.py`](numerical-methods/monte_carlo_area.py) · [`numerical-methods/monte_carlo_3d.py`](numerical-methods/monte_carlo_3d.py)

Area estimation between two curves using Monte Carlo sampling. 3D variant estimates π by sampling points inside a unit sphere.

### 🔵 Sorting Algorithm Benchmark
[`algorithms/sorting_benchmark.py`](algorithms/sorting_benchmark.py)

Empirical runtime comparison of Bubble Sort, Selection Sort, and Quick Sort across array sizes [100, 1600]. Results plotted on log-log scale to confirm O(n²) vs O(n log n) complexity.

### 🔵 Jacobi Iterative Solver
[`numerical-methods/jacobi_general.py`](numerical-methods/jacobi_general.py)

General n×n Jacobi solver for diagonally dominant linear systems. Separate 2×2 implementation tracks convergence rate as a function of tolerance (ε from 10⁻² to 10⁻⁸).

### 🔵 Image Processing
[`image-processing/`](image-processing/)

Manual implementation of cross-shaped and 3×3 kernel smoothing filters. Binary segmentation via thresholding for aggregate fraction detection in grayscale images.

---

## Running

```bash
pip install numpy matplotlib scipy
python simulations/nbody_simulation.py
```

Each script is self-contained and can be run independently.
