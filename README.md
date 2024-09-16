#### NAME: PABITRA BHANDARI
#### COURSE: MSCS_532 ALGORITHMS AND DATA STRUCTURES
#### DATE: 09/15/2024
---
# Assignment 4: Heap Data Structures - Implementation, Analysis, and Applications

## Overview
This assignment involves implementing a priority queue using heap data structures and analyzing their performance. The project is divided into two main parts:
1. **Part 1: Heapsort Implementation and Analysis**
2. **Part 2: Priority Queue Implementation and Scheduler Simulation**

### Part 1: Heapsort Implementation
In Part 1, the Heapsort algorithm was implemented using a max-heap to efficiently sort an array. The implementation involved building the heap, extracting the maximum element, and maintaining the heap property. The time complexity of Heapsort is **O(n log n)** in all cases (worst, average, and best), and it operates in-place with **O(1)** space complexity. The comparison of Heapsort with Quicksort and Merge Sort showed that Quicksort is generally faster for random data but can perform poorly on sorted and reverse-sorted data due to its **O(n^2)** worst-case complexity.

### Part 2: Priority Queue Implementation
In Part 2, a priority queue was implemented using a max-heap to manage tasks based on their priority. The priority queue supports core operations like:
- **Insert**: O(log n)
- **Extract Max**: O(log n)
- **Increase Key**: O(log n)
- **is_empty**: O(1)

Tasks with the highest priority are extracted first, making the max-heap suitable for scheduling algorithms. The time complexity analysis shows that the priority queue implementation is efficient and scalable.

---

### Instructions to run code:
#### Running on windows 
1. Open a terminal (command prompt).
2. Navigate to the folder containing the python script using:

   ```bash
   cd path/to/your/script
   ```

3. Run the python file using:

   ```bash
   python your_script_name.py
   ```

#### Running on MacOS (Linux)
1. Open a terminal
2. Navigate to the folder containing the python script using:

   ```bash
   cd path/to/your/script
   ```

3. Run the python file using:

    ```bash
   python3 your_script_name.py
   ```

### Files:
- **Heapsort_report.md**: Contains detailed Heapsort implementation, analysis and comparison report.
- **priority_queue.py**: Contains the code for the priority queue implementation using a max-heap.
- **comparison.py**: Contains the code for comparison of the run time of heapsort algorithm with other sorting algorithms like quicksort and mergesort.
- **priority_queue.md**: Detailed report on the priority queue design, time complexity analysis, and core operations.

---

## Summary of Findings:
- **Heapsort** guarantees **O(n log n)** performance in all cases, making it predictable but slightly slower than Quicksort on random data.
- **Priority Queue** implemented with a **max-heap** efficiently manages tasks, with high-priority tasks being processed first. The time complexity for key operations like insertion, extraction, and priority modification remains logarithmic, making it suitable for real-time scheduling tasks.
