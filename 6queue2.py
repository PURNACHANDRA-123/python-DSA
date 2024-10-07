from collections import deque

class queueusingdqueue:
    def __init__(self):
        self.queue=deque()
    def enqueue(self,val):
        self.queue.append(val)
    def dequeue(self):   #(first item added is removed first — FIFO)
        if not self.is_empty():
            remove=self.queue.popleft()
            return remove
        else:
            print("queue is empty")
    def is_empty(self):
        return len(self.queue)==0
    def peek(self):
        if not self.is_empty():
            return self.queue[0]
        else:
            return "Queue is empty!"
    def length(self):
        return len(self.queue)
      

q1=queueusingdqueue()
q1.enqueue(10)
q1.enqueue(60)
q1.enqueue(90)
print(f"Front item: {q1.peek()}")
q1.dequeue()
print(f"front item: {q1.peek()}")
print(f"length is {q1.length()}")











