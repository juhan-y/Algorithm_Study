# 11866 요세푸스 문제 0
import sys
from collections import deque

queue = deque()
li = []

N, K = map(int, sys.stdin.readline().split())

for i in range(1, N+1):
    queue.append(i)

while queue:
    for i in range(K-1):
        queue.append(queue.popleft())
    li.append(queue.popleft())

print('<', end='')
print(', '.join(map(str, li)), end='')
print('>')
