

class HashTable:
    def __init__(self, size):
        self.size = 10
        self.array = [None] * self.size

    def get_hash(self, key):
        hash_value = 0
        for char in key:
            hash_value += ord(char)
        return hash_value % self.size
    def insert(self, key, value):
        hash_value=self.get_hash(key)
        self.array[hash_value]=value
    def search(self, key):
        hash_value=self.get_hash(key)
        return self.array[hash_value]
    

t=HashTable(10)
t.insert("apple", 45)
t.insert("banana", 2)
t.insert("cherry", 3)
print(t.search("apple"))
