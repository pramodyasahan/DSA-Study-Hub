class CircularNode:
    def __init__(self, data):
        self.data = data
        self.next = None


class CircularLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_end(self, data):
        new_node = CircularNode(data)
        if not self.head:
            self.head = new_node
            self.head.next = self.head
        else:
            current = self.head
            while current.next != self.head:
                current = current.next
            current.next = new_node
            new_node.next = self.head

    def delete(self, data):
        if not self.head:
            print(f"Value {data} not found")
            return

        current = self.head
        previous = None

        while True:
            if current.data == data:
                if previous:
                    previous.next = current.next
                    if current == self.head:
                        self.head = previous.next
                else:
                    tail = self.head
                    while tail.next != self.head:
                        tail = tail.next
                    tail.next = current.next
                    self.head = current.next
                return

            previous = current
            current = current.next
            if current == self.head:
                break

        print(f"Value {data} not found")

    def search(self, data):
        if not self.head:
            return False

        current = self.head
        while True:
            if current.data == data:
                return True
            current = current.next
            if current == self.head:
                break
        return False

    def display(self):
        if not self.head:
            return
        current = self.head
        while True:
            print(current.data, end=' -> ')
            current = current.next
            if current == self.head:
                break
        print('(Back to head)')


# Example usage
cll = CircularLinkedList()
cll.insert_at_end(1)
cll.insert_at_end(2)
cll.insert_at_end(3)
cll.display()

print("Searching for 2:", cll.search(2))
cll.delete(2)
cll.display()
