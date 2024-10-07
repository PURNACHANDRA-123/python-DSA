class Binarysearchtree:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
    def insert(self,value):
        if value < self.data: # Go left
            if self.left is None:
                self.left=Binarysearchtree(value)
            else:
                self.left.insert(value)
        elif value > self.data:  #go right
            if self.right is None:
                self.right=Binarysearchtree(value)
            else:
                self.right.insert(value)
    
    def search(self,value):
        if value ==self.data:
            return True
        elif value < self.data and self.left: #value might be in left subtree
            return self.left.search(value)
        elif value > self.data and self.right:  #value might be in right subtree
            return self.right.search(value)
        return False
    def find_max(self):
        if self.right is None:
            return self.data
        else:
            return self.right.find_max()

    def find_min(self):
        if self.left is None:
            return self.data
        else:
            return self.left.find_min()
    def delete(self,value):
        if value <self.data:
            if self.left:
                self.left=self.left.delete(value)
        elif value > self.data:
            if self.right:
                self.right=self.right.delete(value)
        else:
            if self.left is None and self.right is None:
                return None
            if self.left is None:
                return self.right
            if self.right is None:
                return self.left
            min_value=self.right.find_min()
            self.data=min_value
            self.right=self.right.delete(min_value)
        return self
root = Binarysearchtree(8)
root.insert(3)
root.insert(10)
root.insert(1)
root.insert(6)
root.insert(4)
root.insert(7)
root.insert(14)
root.insert(13)

# Search for a value in the BST
print(root.search(6))  # Output: True
print(root.search(15))  # Output: False

#time complexity O(log n)
print(root.find_max())
print(root.find_min())
root.delete(6)
print(root.search(6))