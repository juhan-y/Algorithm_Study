# bfs 풀이법
from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
count = 0

def bfs(x, y):
    queue = deque(())
    queue.append((x, y))

    if graph[x][y] == 1:
        return 0

    while queue:
        x, y = queue.popleft()
        graph[x][y] = 1
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            if graph[nx][ny] == 0:
                queue.append((nx, ny))
    return 1


n, m = map(int, input().split())
graph = []
for i in range(n):
    graph.append(list(map(int, input())))

for i in range(n):
    for j in range(m):
        count += bfs(i, j)

print(count)
