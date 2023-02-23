from collections import deque

n = int(input())

graph = [[] for _ in range(n+1)]

for _ in range(n-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

dic = {}
dic[1] = 1

def bfs(node):
    q = deque()
    q.append(node)
    visited[node] = True
    while q:
        new = q.popleft()
        for i in graph[new]:
            if not visited[i]:
                dic[i] = new
                q.append(i)
                visited[i] = True


visited = [False] * (n+1)
bfs(1)

for i in range(2, n+1):
    print(dic[i])