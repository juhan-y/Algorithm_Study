import sys
from collections import deque
input = sys.stdin.readline
n, m = map(int, input().split())

graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False] * (n+1)

def bfs(k):
    q = deque()
    q.append(k)
    while q:
        now = q.popleft()
        for x in graph[now]:
            if not visited[x]:
                visited[x] = True
                q.append(x)
            

ans = 0
for i in range(1, n+1):
    if not visited[i]:
        ans += 1
        visited[i] = True
        bfs(i)

print(ans)