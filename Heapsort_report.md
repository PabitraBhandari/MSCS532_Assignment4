# Heapsort Implementation and Analysis
## Implementation
Heapsort algorithm using python is implement in this [file](./heapsort_algorithm.py). In clear and efficient way, the correct steps has been implemented for building a max-heap, extracting the maximum element, and maintaining the heap property.

## Analysis
The implemented heapsort algorithm has been analyzed below, providing rigorous analysis of the time complexity of Heapsort in the worst, average, and best cases. It is discussed with the space complexity and any additional overheads.

### Time Complexity

The **time complexity** of Heapsort is derived from two main stages: building the max-heap and sorting the array by extracting the maximum element.

1. **Building the Max-Heap**:
   - The **BUILD-MAX-HEAP** procedure constructs a max-heap from an unsorted array by calling **MAX-HEAPIFY** on every non-leaf node, working from the bottom of the heap upwards. According to the textbook, "BUILD-MAX-HEAP goes through the remaining nodes of the tree and runs MAX-HEAPIFY on each one" (Cormen et al., 2022, p. 167).
   - **Heapify Operation**: Each call to `MAX-HEAPIFY` takes **O(log n)** time in the worst case, as the node may need to move from the root to a leaf node to maintain the max-heap property.
   - **Total Time**: Although there are approximately `n/2` nodes that need to be heapified, most nodes are near the bottom of the tree and require less work. As a result, building the heap takes **O(n)** time, as it is explained that “the running time is O(n)” (Cormen et al., 2022, p. 169).

2. **Heapsort (Extracting Elements)**:
   - After the heap is built, the **HEAPSORT** procedure repeatedly extracts the largest element from the heap (the root), places it at the end of the array, and then heapifies the reduced heap. Cormen et al. (2022) state that "the procedure HEAPSORT, which runs in O(n log n) time, sorts an array in place" (p. 163).
   - Each extraction involves a **heapify** operation, which takes **O(log n)** time, and we perform this operation for each of the `n` elements. Thus, the extraction phase takes **O(n log n)** time (Cormen et al., 2022, p. 169).

#### Summary of Time Complexity:
- **Best Case**: **O(n log n)**
- **Average Case**: **O(n log n)**
- **Worst Case**: **O(n log n)**

Heapsort’s time complexity remains **O(n log n)** in all cases because the algorithm doesn’t take advantage of already sorted data, and every step involves logarithmic-time heap operations (Cormen et al., 2022, p. 163).

---

### Space Complexity

Heapsort is an **in-place sorting algorithm**, meaning it uses a constant amount of extra space beyond the input array.

- **Auxiliary Space**: The algorithm primarily modifies the input array directly, so it requires **O(1)** auxiliary space.
- **Recursive Overhead**: If `MAX-HEAPIFY` is implemented recursively, there could be additional overhead on the call stack. In this case, the depth of recursion is bounded by the height of the heap, which is **O(log n)**. However, this can be avoided by using an iterative version of `MAX-HEAPIFY`, which would reduce the space overhead to **O(1)** (Cormen et al., 2022, p. 163).

Thus, the **space complexity** of Heapsort is **O(1)** for in-place sorting, or **O(log n)** if recursion is used for heapify.

---

## Conclusion

- **Time Complexity**: O(n log n) in all cases (best, average, and worst).
- **Space Complexity**: O(1) auxiliary space (O(log n) with recursion).

Heapsort is a reliable and space-efficient sorting algorithm, especially suitable when space is at a premium. However, it is not a stable sort, and the constant factors in its time complexity might make it slower than other **O(n log n)** algorithms like Quicksort in practice (Cormen et al., 2022, p. 163).

---

## Example Code Output:

```
Original array: [19, 1, 10, 14, 16, 7, 8, 5, 3, 12, 9]
Sorted array:   [1, 3, 5, 7, 8, 9, 10, 12, 14, 16, 19]
```
---

## Comparison of running time of Heapsort with QuickSort and MergeSort
- Running time of Heapsort is compared with Quicksort and Mergesort in this [file](./comparison.py).
- This is the sample output of the program:

### Input Size: 1000

| Input Condition | Heapsort (s) | Quicksort (s) | Merge Sort (s) |
|-----------------|--------------|---------------|----------------|
| Random          | 0.001804     | 0.001079      | 0.001343       |
| Sorted          | 0.001917     | 0.000800      | 0.000970       |
| Reverse_sorted  | 0.001669     | 0.000805      | 0.000947       |

### Input Size: 5000

| Input Condition | Heapsort (s) | Quicksort (s) | Merge Sort (s) |
|-----------------|--------------|---------------|----------------|
| Random          | 0.011305     | 0.005777      | 0.007924       |
| Sorted          | 0.014908     | 0.005648      | 0.005614       |
| Reverse_sorted  | 0.014476     | 0.005415      | 0.005687       |

### Input Size: 10000

| Input Condition | Heapsort (s) | Quicksort (s) | Merge Sort (s) |
|-----------------|--------------|---------------|----------------|
| Random          | 0.023728     | 0.012266      | 0.022326       |
| Sorted          | 0.030165     | 0.009864      | 0.011096       |
| Reverse_sorted  | 0.021434     | 0.009816      | 0.016510       |


**below is the discussion of Observed Results nad Theoretical Analysis:**

### 1. General Trends

- **Quicksort** generally outperforms Heapsort and Merge Sort, especially with smaller input sizes and random data. 
- **Heapsort** is consistent across all distributions, but it is slightly slower than Quicksort for random and sorted data.
- **Merge Sort** is slower than the other algorithms, especially for smaller inputs, due to its higher constant factors.

### 2. Performance Based on Input Distributions

- **Random Distribution**: Quicksort performs the best due to its average-case time complexity of **O(n log n)**, while Heapsort and Merge Sort follow behind. This reflects the efficiency of Quicksort's partitioning on random data.
- **Sorted and Reverse-Sorted Distributions**: Quicksort's performance degrades, especially on larger reverse-sorted data, where it approaches its worst-case time complexity of **O(n²)**. Heapsort, on the other hand, maintains its consistent **O(n log n)** performance in all cases, unaffected by input order.

### 3. Space Complexity Consideration

- **Heapsort**: In-place and uses **O(1)** auxiliary space, making it efficient in terms of memory.
- **Merge Sort**: Requires **O(n)** extra space for the merge process, contributing to its slower performance on smaller inputs.
- **Quicksort**: In-place but incurs **O(log n)** space overhead due to recursion.

### Conclusion

- **Quicksort** excels for random data but struggles on reverse-sorted data due to its worst-case performance.
- **Heapsort** offers consistent performance across all input types, making it reliable.
- **Merge Sort** is slower due to memory overhead but remains consistent across input distributions.

---

**References**:
- Cormen, T. H., Leiserson, C. E., Rivest, R. L., & Stein, C. (2022). *Introduction to algorithms* (4th ed.). MIT Press.
