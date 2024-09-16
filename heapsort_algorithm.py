"""
This Python script implements the Heapsort algorithm. It first converts an unsorted array into a max-heap,
and then repeatedly extracts the largest element from the heap (the root) and places it at the end of the array.
The algorithm maintains the max-heap property during this process, ensuring that the array is sorted in ascending order.
Heapsort is an in-place, comparison-based sorting algorithm with a time complexity of O(n log n).
"""

def sift_down(arr, start, end):
    # This function ensures the heap property is maintained from 'start' to 'end'
    root = start

    while True:
        child = 2 * root + 1  # Left child index
        if child > end:
            break
        # Check if the right child exists and is greater than the left child
        if child + 1 <= end and arr[child] < arr[child + 1]:
            child += 1
        # If the root is smaller than the largest child, swap them
        if arr[root] < arr[child]:
            arr[root], arr[child] = arr[child], arr[root]
            root = child  # Move down to the child position
        else:
            break

def heapify(arr):
    # Turn the array into a max-heap by sifting down each non-leaf node
    count = len(arr)
    start = (count - 2) // 2  # Start with the last non-leaf node
    while start >= 0:
        sift_down(arr, start, count - 1)
        start -= 1

def heapsort(arr):
    # First, build the max-heap
    heapify(arr)
    count = len(arr)

    # Repeatedly extract the maximum element and shrink the heap
    end = count - 1
    while end > 0:
        arr[end], arr[0] = arr[0], arr[end]  # Swap the root (maximum) with the last item
        end -= 1  # Reduce the size of the heap
        sift_down(arr, 0, end)  # Restore heap property

# Example usage
if __name__ == "__main__":
    test_array = [19, 1, 10, 14, 16, 7, 8, 5, 3, 12, 9]
    print("Original array:", test_array)
    heapsort(test_array)
    print("Sorted array:  ", test_array)
