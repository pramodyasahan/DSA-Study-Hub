class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        return None

    def peek(self):
        if not self.is_empty():
            return self.items[0]
        return None

    def is_empty(self):
        return len(self.items) == 0

    def search(self, item):
        try:
            return self.items.index(item)
        except ValueError:
            return -1


# Example usage
queue = Queue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
print(queue.peek())  # Output: 1
print(queue.dequeue())  # Output: 1
print(queue.search(2))  # Output: 0
print(queue.items)  # Output: [2, 3]
