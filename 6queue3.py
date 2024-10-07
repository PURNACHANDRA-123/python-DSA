import queue
q3=queue.Queue()

q3.put(90)  #enqueue
q3.put(60)
q3.put(80)
q3.put(70)

print(f"front item: {q3.queue[0]}")
print(f"Queue size: {q3.qsize()}")

q3.get()  #dequeue
print(f"Queue size: {q3.qsize()}")

#is empty
print(q3.empty())

