#collision handling
class HashTableChaining:
    def __init__(self, size):
        self.size = size
        # Each slot in the table is initialized to an empty list
        self.table = [[] for _ in range(size)]
    
    def hash_function(self, key):
        """Simple hash function using sum of ASCII values mod size"""
        return sum(ord(c) for c in key) % self.size
    
    def insert(self, key, value):
        """Inserts a key-value pair into the hash table using chaining"""
        index = self.hash_function(key)
        # Check if the key already exists in the chain (list) at that index
        for i, (k, v) in enumerate(self.table[index]):
            if k == key:
                # If the key exists, update its value
                self.table[index][i] = (key, value)
                return v
        
        # If key does not exist, append the new key-value pair to the list
        self.table[index].append((key, value))
    
    def get(self, key):
        """Retrieves the value for the given key using chaining"""
        index = self.hash_function(key)
        # Search for the key in the chain (list) at the calculated index
        for k, v in self.table[index]:
            if k == key:
                return v
         
        # If key is not found, return None
        return None
    
    def delete(self, key):
        """Deletes a key-value pair from the hash table using chaining"""
        index = self.hash_function(key)
        # Search for the key in the chain (list) at the calculated index
        for i, (k, v) in enumerate(self.table[index]):
            if k == key:
                # Remove the key-value pair from the list
                del self.table[index][i]
                return v

# Example usage:
ht_chain = HashTableChaining(10)

# Inserting key-value pairs
ht_chain.insert("apple", "fruit")
ht_chain.insert("carrot", "vegetable")
ht_chain.insert("banana", "fruit")
ht_chain.insert("lemon", "fruit")  # May cause a collision, but will be stored in the list
#insert with same key another then lemon
ht_chain.insert("lemon", "vegetable")
# Retrieving values
print(ht_chain.get("lemon")) # Output: fruit
#here overwrite
ht_chain.delete("banana")
print(ht_chain.get("banana")) # Output: None
ht_chain.insert("strawberry", "fruit")
print(ht_chain.get("strawberry")) # Output: fruit
print(ht_chain.get("kalam")) # Output: None