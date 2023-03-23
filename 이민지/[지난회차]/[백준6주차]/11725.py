# # 방법 1 : dfs
import sys
sys.setrecursionlimit(10**6)

def dfs(v):
    for i in graph[v]:
        if visited[i] == 0:
            visited[i] = v
            dfs(i)

input = sys.stdin.readline
n = int(input())
graph = [[] for _ in range(n+1)]
visited = [0] * (n+1)
for _ in range(n-1):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

dfs(1)

for i in range(2,n+1):
    print(visited[i])

#방법 2 : bfs
import sys
from collections import deque

input = sys.stdin.readline

def bfs():
    while queue:
        v = queue.popleft()
        for i in graph[v]:
            if visited[i] == 0:
                queue.append(i)
                visited[i] = v

n = int(input())
graph = [[] for _ in range(n+1)]
visited = [0] * (n+1)

for _ in range(n-1):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

queue = deque([1])

bfs()

for i in range(2,n+1):
    print(visited[i])