"""
This script empirically compares the performance of three sorting algorithms: Heapsort, Quicksort, and Merge Sort.
The script runs each sorting algorithm on arrays of various sizes (1000, 5000, and 10000) and different input distributions:
- Random
- Already sorted
- Reverse sorted
For each input distribution and size, the script measures the time taken by each algorithm to sort the array.
The results are printed in a horizontal format for easy comparison, showing the sorting times for Heapsort, Quicksort, and Merge Sort side by side.
"""

import time
import random

# Heapsort implementation
def heapify(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[left] > arr[largest]:
        largest = left

    if right < n and arr[right] > arr[largest]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

def heapsort(arr):
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)

# Quicksort implementation
def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)

# Merge Sort implementation
def mergesort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = mergesort(arr[:mid])
    right = mergesort(arr[mid:])
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

# Function to measure sorting time
def measure_time(sort_fn, arr):
    start_time = time.time()
    sort_fn(arr)
    return time.time() - start_time

# Input size and distributions
sizes = [1000, 5000, 10000]
distributions = ["random", "sorted", "reverse_sorted"]

for size in sizes:
    print(f"Input Size: {size}")
    
    for dist in distributions:
        if dist == "random":
            arr = [random.randint(0, size) for _ in range(size)]
        elif dist == "sorted":
            arr = list(range(size))
        elif dist == "reverse_sorted":
            arr = list(range(size, 0, -1))
        
        # Measure Heapsort time
        heap_arr = arr.copy()
        heap_time = measure_time(heapsort, heap_arr)
        
        # Measure Quicksort time
        quick_arr = arr.copy()
        quick_time = measure_time(quicksort, quick_arr)
        
        # Measure Merge Sort time
        merge_arr = arr.copy()
        merge_time = measure_time(mergesort, merge_arr)
        
        # Print in horizontal format
        print(f"  {dist.capitalize()}:   Heapsort: {heap_time:.6f} s | Quicksort: {quick_time:.6f} s | Merge Sort: {merge_time:.6f} s")
    
    print()  # For separating different input sizes
