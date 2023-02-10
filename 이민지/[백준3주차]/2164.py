from collections import deque

n = int(input())
graph = list(range(1,n+1))
queue = deque(graph)

while len(queue) > 1:
    queue.popleft()
    if len(queue) == 1:
        break
    a = queue.popleft()
    queue.append(a)

print(queue[0])
