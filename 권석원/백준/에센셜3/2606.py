import sys
from collections import deque

computer_cnt = int(sys.stdin.readline())
N = int(sys.stdin.readline())

graph = [[] for _ in range(computer_cnt+1)]
virus = [0 for _ in range(computer_cnt+1)]

q = deque()

for _ in range(N):
    pc1, pc2 = map(int,sys.stdin.readline().split())
    graph[pc1].append(pc2)
    graph[pc2].append(pc1)

q.append(1)

while q:
    k = q.popleft()

    if virus[k]:
        continue

    virus[k] = 1

    for i in graph[k]:
        if virus[i] == 0:
            q.append(i)

print(virus.count(1)-1)
