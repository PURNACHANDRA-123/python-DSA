#last in first out data structure
class Stack:
    def __init__(self):
        self.items = []  # Initialize the stack with an empty list

    def push(self, item):
        """Add element to the top of the stack."""
        self.items.append(item)

    def pop(self):
        """Remove and return the top element from the stack."""
        # Fix: Call the method self.is_empty() with parentheses
        if not self.is_empty():
            return self.items.pop()  # Return the top item (last one in the list)
        return "Stack is empty"

    def peek(self):
        """Return the top element without removing it."""
        # Fix: Call the method self.is_empty() with parentheses
        if not self.is_empty():
            return self.items[-1]  # Return the top element without removing it
        return "Stack is empty"

    def is_empty(self):
        """Check if the stack is empty."""
        return len(self.items) == 0  # Return True if the list is empty

    def size(self):
        """Return the number of elements in the stack."""
        return len(self.items)

# Create a stack instance
s1 = Stack()

# Push elements into the stack
s1.push(12)
s1.push(24)
s1.push(36)

# Check the size of the stack
print("Stack size:", s1.size())  # Output: Stack size: 3

# Peek the top element
print("Top element:", s1.peek())  # Output: Top element: 36

# Pop the top element
print("Popped element:", s1.pop())  # Output: Popped element: 36
print("Top element:", s1.peek())
print("length is",s1.size())