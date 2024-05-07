class Queue:
    def __init__(self):
        self.items = []  # using list to store queue elements

    def is_empty(self):
        """Check if the queue is empty."""
        return len(self.items) == 0

    def enqueue(self, item):
        """Add an item to the rear of the queue."""
        self.items.append(item)

    def dequeue(self):
        """Remove and return the front item of the queue. Raises IndexError if the queue is empty."""
        if self.is_empty():
            raise IndexError("dequeue from empty queue")
        return self.items.pop(0)  # remove the first item

    def peek(self):
        """Return the front item of the queue without removing it. Raises IndexError if the queue is empty."""
        if self.is_empty():
            raise IndexError("peek from empty queue")
        return self.items[0]

    def size(self):
        """Return the number of items in the queue."""
        return len(self.items)

    def display(self):
        """Display the entire queue from front to rear."""
        print("Queue contents (front to rear):", self.items)

# Example usage
queue = Queue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
queue.display()  # Display queue contents

print("Front item:", queue.peek())  # Peek at the front item
print("Dequeued item:", queue.dequeue())  # Dequeue the front item
queue.display()  # Display queue contents after dequeue

try:
    print(queue.dequeue())
    print(queue.dequeue())
    print(queue.dequeue())  # This should raise an error as the queue will be empty
except IndexError as e:
    print(e)  # Handling empty queue error
