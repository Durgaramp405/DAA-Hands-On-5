import time
import random
import matplotlib.pyplot as plt
import numpy as np

def median_of_three(arr, low, high):
    mid = (low + high) // 2
    a, b, c = arr[low], arr[mid], arr[high]
    if a > b:
        if a < c:
            return low
        elif b > c:
            return mid
        else:
            return high
    else:
        if a > c:
            return low
        elif b < c:
            return mid
        else:
            return high

def partition(arr, low, high):
    pivot_index = median_of_three(arr, low, high)
    arr[pivot_index], arr[high] = arr[high], arr[pivot_index]  # Move pivot to end
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def quicksort(arr, low, high):
    while low < high:
        pi = partition(arr, low, high)
        if pi - low < high - pi:
            quicksort(arr, low, pi - 1)
            low = pi + 1  # Tail call optimization
        else:
            quicksort(arr, pi + 1, high)
            high = pi - 1

def best_case(size):
    return list(range(size))  # Already sorted

def worst_case(size):
    return list(range(size, 0, -1))  # Reversed order

def average_case(size):
    return [random.randint(0, size) for _ in range(size)]

def benchmark_quicksort(arr_sizes, case):
    times = []
    for size in arr_sizes:
        if case == 'best':
            arr = best_case(size)
        elif case == 'worst':
            arr = worst_case(size)
        else:
            arr = average_case(size)
        
        start_time = time.time()
        quicksort(arr, 0, len(arr) - 1)
        end_time = time.time()
        times.append(end_time - start_time)
    return times

arr_sizes = [1000, 5000, 10000, 15000, 20000, 25000]

best_case_times = benchmark_quicksort(arr_sizes, 'best')
worst_case_times = benchmark_quicksort(arr_sizes, 'worst')
average_case_times = benchmark_quicksort(arr_sizes, 'average')

plt.figure(figsize=(10, 6))
plt.plot(arr_sizes, best_case_times, label='Best Case', marker='o')
plt.plot(arr_sizes, worst_case_times, label='Worst Case', marker='s')
plt.plot(arr_sizes, average_case_times, label='Average Case', marker='^')
plt.xlabel('Input Size (n)')
plt.ylabel('Time (seconds)')
plt.legend()
plt.title('Quicksort Performance')
plt.grid()
plt.show()
