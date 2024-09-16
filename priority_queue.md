# Part 2: Priority Queue Implementation Report

## 1. Data Structure

### Choice of Data Structure:
In this implementation, a **list (array)** was chosen to represent the binary heap. This is because a list allows for efficient heap operations:
- The parent and child relationships in a binary heap are easily managed with a list. The parent of a node at index `i` can be found at `floor((i-1)/2)`, and the children are located at `2i + 1` (left child) and `2i + 2` (right child).
- A list-based heap enables both **insertion** and **extraction** in **O(log n)** time, which is crucial for maintaining the heap property efficiently.

### Task Class Design:
A `Task` class was designed to represent individual tasks, with attributes such as:
- `task_id`: A unique identifier for each task.
- `priority`: The priority of the task, which is the value used to determine the task’s position in the heap.
- `arrival_time`: When the task was added to the queue.
- `deadline`: The deadline by which the task must be completed.

This class provides a structured way to manage the relevant task information and to easily represent and manipulate tasks within the priority queue.

### Max-Heap vs. Min-Heap:
A **max-heap** was chosen for this implementation, where tasks with the highest priority values are processed first. This decision aligns with scheduling algorithms that prioritize tasks with higher importance or urgency. In a max-heap, the root always contains the task with the highest priority, ensuring that high-priority tasks are quickly accessible.

## 2. Core Operations

### 2.1 Insert Operation:
- **Implementation**: 
  The `insert(task)` method adds a new task to the heap by appending it to the list. To maintain the heap property, a helper function `_bubble_up()` is called, which compares the newly added task’s priority with its parent and moves the task up the heap if necessary.
  
- **Time Complexity**: 
  The insertion operation takes **O(log n)** time because, in the worst case, the newly inserted task might need to move all the way up to the root to restore the heap property. Each comparison is done between the child and parent, and since the height of the heap is proportional to **log n**, the time complexity is logarithmic.

### 2.2 Extract Max Operation:
- **Implementation**: 
  The `extract_max()` method removes and returns the task with the highest priority, which is always located at the root of the heap. The last element in the heap is swapped with the root, and the heap property is restored using the `_bubble_down()` method. This function compares the new root with its children and moves it down the heap as necessary to ensure the heap property is maintained.
  
- **Time Complexity**: 
  The extraction operation also takes **O(log n)** time because the task might need to move all the way down the heap to maintain the max-heap property.

### 2.3 Increase Key Operation:
- **Implementation**: 
  The `increase_key(task, new_priority)` method modifies the priority of an existing task and restores the heap property by calling `_bubble_up()`. The priority of the task is increased, and the task is moved up the heap if its new priority is higher than its parent.
  
- **Time Complexity**: 
  This operation takes **O(log n)** because the task may need to move up the heap, which takes time proportional to the height of the heap.

### 2.4 is_empty Operation:
- **Implementation**: 
  The `is_empty()` method is a simple check that returns `True` if the heap is empty and `False` otherwise. This is done by checking the length of the list representing the heap.
  
- **Time Complexity**: 
  This operation takes **O(1)** time since it only checks the length of the heap.

## Deliverables:

### 1. Source Code:
The [source code](./priority_queue.py) is well-documented and includes the following operations: insert, extract_max, increase_key, and is_empty. Each operation is labeled, and helper methods (`_bubble_up`, `_bubble_down`) are used to restore the heap property efficiently.

### 2. Report Discussion and Design Choices:
- The decision to use a list for the heap ensures efficient heap operations with **O(log n)** insertion and extraction times.
- The max-heap structure was chosen to align with scheduling algorithms that prioritize high-importance tasks.
- The `Task` class was designed to hold all necessary task-related data, allowing for efficient management of tasks within the queue.

### 3. Time Complexity Analysis:
Each operation was carefully analyzed for its time complexity:
- **Insert**: O(log n)
- **Extract Max**: O(log n)
- **Increase Key**: O(log n)
- **is_empty**: O(1)

This analysis shows that the priority queue operations are efficient and scalable, making this implementation suitable for real-world scheduling scenarios.
