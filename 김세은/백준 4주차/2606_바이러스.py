# 2606 바이러스
import sys
from collections import deque

N = int(input())
M = int(input())

graph = [[] for _ in range(N+1)]
for i in range(M):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [0] * (N+1)

def bfs(graph, start, visited):
    cnt = 0

    q = deque([start])
    visited[start] = cnt

    while q:
        v = q.popleft()

        for i in graph[v]:
            if visited[i] == 0:
                cnt += 1
                q.append(i)
                visited[i] = cnt

bfs(graph, 1, visited)
print(max(visited)-1)
