'''
Program Description:
This script implements a priority queue using a max-heap data structure, represented by a list. The max-heap allows for efficient insertion, extraction of the highest priority task, and updating task priorities. The priority queue is used to manage tasks based on their priority, where tasks with the highest priority are processed first. The program includes core operations like insert, extract_max, increase_key, and checking if the queue is empty.

Part 2: Priority Queue Implementation
- Step 1: Data Structure - Using a list to represent a binary max-heap.
- Step 2: Core Operations - Insert, extract_max, increase_key, and is_empty methods.
'''

# Task class representing individual tasks in the priority queue
class Task:
    def __init__(self, task_id, priority, arrival_time, deadline):
        self.task_id = task_id
        self.priority = priority
        self.arrival_time = arrival_time
        self.deadline = deadline
    
    def __repr__(self):
        return f"Task(ID={self.task_id}, Priority={self.priority})"


# Priority Queue class implemented with a max-heap
class PriorityQueue:
    def __init__(self):
        # The heap is represented as a list (array)
        self.heap = []
    
    # Insert Operation
    def insert(self, task):
        # Insert a new task into the priority queue and restore the heap property.
        self.heap.append(task)
        self._bubble_up(len(self.heap) - 1)

    # Extract Max Operation
    def extract_max(self):
        # Remove and return the task with the highest priority.
        if self.is_empty():
            return None
        max_task = self.heap[0]
        self.heap[0] = self.heap.pop()  # Replace root with the last element
        self._bubble_down(0)
        return max_task

    # Increase Key Operation
    def increase_key(self, index, new_priority):
        # Increase the priority of a task and restore the heap property.
        if new_priority < self.heap[index].priority:
            raise ValueError("New priority must be greater than the current priority")
        self.heap[index].priority = new_priority
        self._bubble_up(index)

    # Is Empty Operation
    def is_empty(self):
        #Check if the priority queue is empty.
        return len(self.heap) == 0

    # Helper method to maintain the heap property during insertion (bubble up)
    def _bubble_up(self, index):
        parent = (index - 1) // 2
        while index > 0 and self.heap[index].priority > self.heap[parent].priority:
            self.heap[index], self.heap[parent] = self.heap[parent], self.heap[index]
            index = parent
            parent = (index - 1) // 2

    # Helper method to maintain the heap property during extraction (bubble down)
    def _bubble_down(self, index):
        n = len(self.heap)
        while True:
            left = 2 * index + 1
            right = 2 * index + 2
            largest = index
            
            if left < n and self.heap[left].priority > self.heap[largest].priority:
                largest = left
            if right < n and self.heap[right].priority > self.heap[largest].priority:
                largest = right

            if largest != index:
                self.heap[index], self.heap[largest] = self.heap[largest], self.heap[index]
                index = largest
            else:
                break


# Example Usage
if __name__ == "__main__":
    # Create a priority queue
    pq = PriorityQueue()

    # Insert tasks into the priority queue
    pq.insert(Task(1, 3, "10:00", "12:00"))
    pq.insert(Task(2, 5, "10:05", "11:30"))
    pq.insert(Task(3, 1, "10:10", "12:30"))
    pq.insert(Task(4, 4, "10:15", "12:45"))

    # Display the heap after insertion
    print("\nHeap after insertion:")
    print(f"{'Task ID':<10} {'Priority':<10} {'Arrival Time':<15} {'Deadline':<15}")
    for task in pq.heap:
        print(f"{task.task_id:<10} {task.priority:<10} {'10:00':<15} {'12:00':<15}")

    # Extract the task with the highest priority
    max_task = pq.extract_max()
    print("\nExtracted max:", max_task)

    # Display the heap after extraction
    print("\nHeap after extraction:")
    print(f"{'Task ID':<10} {'Priority':<10} {'Arrival Time':<15} {'Deadline':<15}")
    for task in pq.heap:
        print(f"{task.task_id:<10} {task.priority:<10} {'10:00':<15} {'12:00':<15}")

    # Increase the priority of Task 1
    pq.increase_key(1, 6)

    # Display the heap after increasing priority
    print("\nHeap after increasing priority:")
    print(f"{'Task ID':<10} {'Priority':<10} {'Arrival Time':<15} {'Deadline':<15}")
    for task in pq.heap:
        print(f"{task.task_id:<10} {task.priority:<10} {'10:00':<15} {'12:00':<15}")
