class HashTableOpenAddressing:
    def __init__(self, size=10):
        self.size = size
        self.table = [None] * size

    def _hash(self, key):
        return hash(key) % self.size

    def insert(self, key, value):
        index = self._hash(key)
        while self.table[index] is not None:
            if self.table[index][0] == key:
                self.table[index] = (key, value)
                return
            index = (index + 1) % self.size
        self.table[index] = (key, value)

    def delete(self, key):
        index = self._hash(key)
        while self.table[index] is not None:
            if self.table[index][0] == key:
                self.table[index] = None
                return
            index = (index + 1) % self.size

    def search(self, key):
        index = self._hash(key)
        while self.table[index] is not None:
            if self.table[index][0] == key:
                return self.table[index][1]
            index = (index + 1) % self.size
        return None


# Example usage
hash_table = HashTableOpenAddressing()
hash_table.insert("name", "Bob")
hash_table.insert("age", 30)
print(hash_table.search("name"))  # Output: Bob
print(hash_table.search("age"))  # Output: 30
hash_table.delete("name")
print(hash_table.search("name"))  # Output: None
