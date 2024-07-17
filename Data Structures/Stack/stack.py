class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        return None

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        return None

    def is_empty(self):
        return len(self.items) == 0

    def search(self, item):
        try:
            return self.items.index(item)
        except ValueError:
            return -1


# Example usage
stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
print(stack.peek())  # Output: 3
print(stack.pop())  # Output: 3
print(stack.search(2))  # Output: 1
print(stack.items)  # Output: [1, 2]
