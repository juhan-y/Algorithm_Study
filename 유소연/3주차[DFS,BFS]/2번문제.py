from collections import deque

que = deque()

que.append(5)
que.append(2)
que.append(3)
que.append(7)
que.popleft()
que.append(1)
que.append(4)
que.popleft()

print(que)