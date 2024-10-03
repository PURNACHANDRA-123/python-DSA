from collections import deque
class Stack:
    def __init__(self):
        self.container = deque()

    def push(self, val):
        self.container.append(val)

    def pop(self):
        return self.container.pop()

    def peek(self):
        return self.container[-1]

    def is_empty(self):
        return len(self.container) == 0
    def size(self):
        return len(self.container)

s2=Stack()
s2.push(1)
s2.push(2)
s2.push(3)
s2.push(4)
print(s2.is_empty())
print(s2.pop())
print(s2.peek())
print(s2.pop())
print(s2.size())
print("peek element is",s2.peek())






