queue = []

queue.append(5)
queue.append(2)
queue.append(3)
queue.append(7)
queue.pop(0)
queue.append(1)
queue.append(4)
queue.pop(0)

print(queue)
print(queue[::-1])