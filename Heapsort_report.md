# Heapsort Analysis: Time and Space Complexity

## Time Complexity

The **time complexity** of Heapsort is derived from two main stages: building the max-heap and sorting the array by extracting the maximum element.

1. **Building the Max-Heap**:
   - The **BUILD-MAX-HEAP** procedure constructs a max-heap from an unsorted array by calling **MAX-HEAPIFY** on every non-leaf node, working from the bottom of the heap upwards. According to the textbook, "BUILD-MAX-HEAP goes through the remaining nodes of the tree and runs MAX-HEAPIFY on each one" (Cormen et al., 2022, p. 167).
   - **Heapify Operation**: Each call to `MAX-HEAPIFY` takes **O(log n)** time in the worst case, as the node may need to move from the root to a leaf node to maintain the max-heap property.
   - **Total Time**: Although there are approximately `n/2` nodes that need to be heapified, most nodes are near the bottom of the tree and require less work. As a result, building the heap takes **O(n)** time, as it is explained that “the running time is O(n)” (Cormen et al., 2022, p. 169).

2. **Heapsort (Extracting Elements)**:
   - After the heap is built, the **HEAPSORT** procedure repeatedly extracts the largest element from the heap (the root), places it at the end of the array, and then heapifies the reduced heap. Cormen et al. (2022) state that "the procedure HEAPSORT, which runs in O(n log n) time, sorts an array in place" (p. 163).
   - Each extraction involves a **heapify** operation, which takes **O(log n)** time, and we perform this operation for each of the `n` elements. Thus, the extraction phase takes **O(n log n)** time (Cormen et al., 2022, p. 169).

### Summary of Time Complexity:
- **Best Case**: **O(n log n)**
- **Average Case**: **O(n log n)**
- **Worst Case**: **O(n log n)**

Heapsort’s time complexity remains **O(n log n)** in all cases because the algorithm doesn’t take advantage of already sorted data, and every step involves logarithmic-time heap operations (Cormen et al., 2022, p. 163).

---

## Space Complexity

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

**References**:
- Cormen, T. H., Leiserson, C. E., Rivest, R. L., & Stein, C. (2022). *Introduction to algorithms* (4th ed.). MIT Press.
