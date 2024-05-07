class Stack:
    def __init__(self):
        self.items = []  # using list to store stack elements

    def is_empty(self):
        """Check if the stack is empty."""
        return len(self.items) == 0

    def push(self, item):
        """Add an item to the top of the stack."""
        self.items.append(item)

    def pop(self):
        """Remove and return the top item of the stack. Raises IndexError if the stack is empty."""
        if self.is_empty():
            raise IndexError("pop from empty stack")
        return self.items.pop()

    def peek(self):
        """Return the top item of the stack without removing it. Raises IndexError if the stack is empty."""
        if self.is_empty():
            raise IndexError("peek from empty stack")
        return self.items[-1]

    def size(self):
        """Return the number of items in the stack."""
        return len(self.items)

    def display(self):
        """Display the entire stack."""
        print("Stack contents (top to bottom):", self.items[::-1])  # display top to bottom

# Example usage
stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
stack.display()

print("Top item:", stack.peek())
print("Popped item:", stack.pop())
stack.display()

try:
    print(stack.pop())
    print(stack.pop())
    print(stack.pop())  # This should raise an error as the stack will be empty
except IndexError as e:
    print(e)  # Handling empty stack error
