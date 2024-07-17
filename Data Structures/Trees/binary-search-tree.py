class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def insert(root, key):
    if root is None:
        return BSTNode(key)
    if key < root.value:
        root.left = insert(root.left, key)
    else:
        root.right = insert(root.right, key)
    return root


def search(root, key):
    if root is None or root.value == key:
        return root
    if key < root.value:
        return search(root.left, key)
    return search(root.right, key)


def delete(root, key):
    if root is None:
        return root
    if key < root.value:
        root.left = delete(root.left, key)
    elif key > root.value:
        root.right = delete(root.right, key)
    else:
        if root.left is None:
            return root.right
        elif root.right is None:
            return root.left
        temp = minValueNode(root.right)
        root.value = temp.value
        root.right = delete(root.right, temp.value)
    return root


def minValueNode(node):
    current = node
    while current.left is not None:
        current = current.left
    return current


def inorder_traversal(root):
    if root:
        inorder_traversal(root.left)
        print(root.value, end=" ")
        inorder_traversal(root.right)


# Example usage
root = BSTNode(50)
root = insert(root, 30)
root = insert(root, 20)
root = insert(root, 40)
root = insert(root, 70)
root = insert(root, 60)
root = insert(root, 80)

print("In-order Traversal of the BST:")
inorder_traversal(root)  # Output: 20 30 40 50 60 70 80

# Search for a node
print("\nSearch for 40:")
node = search(root, 40)
print(node.value if node else "Not found")  # Output: 40

# Delete a node
print("\nDelete 20 and in-order traversal:")
root = delete(root, 20)
inorder_traversal(root)  # Output: 30 40 50 60 70 80
