class QueueUsingList:
    def __init__(self):
        self.queue = []

    def enqueue(self, val):
        self.queue.append(val)
        

    def dequeue(self):
        if not self.is_empty():
            removed_item = self.queue.pop(0)
            return removed_item
        else:
            print("queue is empty")
#(first item added is removed first — FIFO)
    def is_empty(self):
        return len(self.queue) == 0

    def length(self):
        return len(self.queue)

    def peek(self):
        if not self.is_empty():
            return self.queue[0]
        else:
            print("queue is empty")

    def size(self):
        return self.length()


q = QueueUsingList()
q.enqueue(10)
q.enqueue(20)
print(f"Front item: {q.peek()}")
q.dequeue()
print(f"Queue size: {q.size()}")


