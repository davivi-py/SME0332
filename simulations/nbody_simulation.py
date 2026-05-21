"""
N-Body Simulation — Velocity Verlet Integrator
===============================================
Simulates a two-body gravitational system using the Velocity Verlet algorithm.
Saves trajectory data to file and plots orbital paths + kinetic energy evolution.

Usage:
    python nbody_simulation.py
"""

import numpy as np
import matplotlib.pyplot as plt


def velocity_verlet(m2):
    """Integrate equations of motion for a two-body system using Velocity Verlet."""
    gamma = 1.0
    dt = 0.01
    m1 = 1.0
    steps = 2000

    r1 = np.array([0.0, 0.0])
    v1 = np.array([0.0, 0.0])
    r2 = np.array([1.0, 0.0])
    v2 = np.array([0.0, 1.0])

    history = np.zeros((steps, 9))
    tn = 0.0

    for n in range(steps):
        r12 = r2 - r1
        dist = np.linalg.norm(r12)
        F = gamma * m2 * m1 / dist**3

        a1 = F * r12 / m1
        a2 = -F * r12 / m2

        r1_new = r1 + v1 * dt + 0.5 * a1 * dt**2
        r2_new = r2 + v2 * dt + 0.5 * a2 * dt**2

        r12_new = r2_new - r1_new
        dist_new = np.linalg.norm(r12_new)
        F_new = gamma * m1 * m2 / dist_new**3

        a1_new = F_new * r12_new / m1
        a2_new = -F_new * r12_new / m2

        v1_new = v1 + 0.5 * (a1 + a1_new) * dt
        v2_new = v2 + 0.5 * (a2 + a2_new) * dt

        history[n] = [tn, r1[0], r1[1], v1[0], v1[1], r2[0], r2[1], v2[0], v2[1]]

        tn += dt
        r1, r2 = r1_new, r2_new
        v1, v2 = v1_new, v2_new

    return history


def simulate_and_save(m2, filename):
    """Run simulation and save trajectory data to a text file."""
    history = velocity_verlet(m2)
    np.savetxt(filename, history, fmt="%.8f")


def load_and_plot(m2, filename):
    """Load saved trajectory and plot orbital paths + kinetic energy."""
    data = np.loadtxt(filename)
    t = data[:, 0]
    r1x, r1y = data[:, 1], data[:, 2]
    v1x, v1y = data[:, 3], data[:, 4]
    r2x, r2y = data[:, 5], data[:, 6]
    v2x, v2y = data[:, 7], data[:, 8]
    m1 = 1.0

    K = 0.5 * m1 * (v1x**2 + v1y**2) + 0.5 * m2 * (v2x**2 + v2y**2)

    plt.figure(figsize=(16, 10))

    plt.subplot(1, 2, 1)
    plt.plot(r1x, r1y, label="Body 1")
    plt.plot(r2x, r2y, label="Body 2")
    plt.title(f"Orbital Trajectories (m2={m2})")
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.legend()
    plt.grid(True)
    plt.axis("equal")

    plt.subplot(1, 2, 2)
    plt.plot(t, K)
    plt.title("Total Kinetic Energy")
    plt.xlabel("Time (t)")
    plt.ylabel("Kinetic Energy")
    plt.grid(True)
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    mass_ratios = [0.001, 0.01, 0.1, 1.0, 2.0]
    for m in mass_ratios:
        fname = f"simulation_m2_{m}"
        simulate_and_save(m, fname)
        load_and_plot(m, fname)
