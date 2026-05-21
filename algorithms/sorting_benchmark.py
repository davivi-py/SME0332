"""
Sorting Algorithm Benchmark
============================
Empirical runtime comparison of Bubble Sort, Selection Sort, and Quick Sort
across array sizes [100, 200, 400, 800, 1600]. Results plotted on a log-log
scale to verify O(n²) vs O(n log n) complexity.

Usage:
    python sorting_benchmark.py
"""

import numpy as np
import matplotlib.pyplot as plt
import time


def bubble_sort(arr):
    """Sort array in-place using Bubble Sort — O(n²)."""
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


def selection_sort(arr):
    """Sort array in-place using Selection Sort — O(n²)."""
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr


def quick_sort(arr):
    """Sort array recursively using Quick Sort — O(n log n) average."""
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)


if __name__ == "__main__":
    sizes = [100, 200, 400, 800, 1600]
    times = {"Bubble Sort": [], "Selection Sort": [], "Quick Sort": []}

    for N in sizes:
        arr = np.random.randint(0, 1000, N).tolist()

        for name, fn in [("Bubble Sort", bubble_sort), ("Selection Sort", selection_sort), ("Quick Sort", quick_sort)]:
            arr_copy = arr.copy()
            t0 = time.time()
            fn(arr_copy)
            times[name].append(time.time() - t0)

    plt.figure(figsize=(10, 6))
    markers = {"Bubble Sort": "o-", "Selection Sort": "s-", "Quick Sort": "^-"}
    for name, t in times.items():
        plt.loglog(sizes, t, markers[name], label=name, linewidth=2)

    plt.xlabel("Array size (N)")
    plt.ylabel("Time (seconds)")
    plt.title("Sorting Algorithm Benchmark (log-log scale)")
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.show()
