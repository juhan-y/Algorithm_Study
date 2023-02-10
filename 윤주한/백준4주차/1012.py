from collections import deque
t = int(input())

dx = [1,0,-1,0]
dy = [0,1,0,-1]

def bfs(graph, visited, i, j, n, m):
    q = deque()
    q.append((i, j))
    visited[i][j] = True
    while q:
        y, x = q.popleft()
        for k in range(4):
            ny = y + dy[k]
            nx = x + dx[k]
            if 0 <= ny < n and 0 <= nx < m:
                if not visited[ny][nx] and graph[ny][nx] == 1:
                    visited[ny][nx] = True
                    q.append((ny, nx))

for _ in range(t):
    m, n, k = map(int, input().split())
    graph = [[0]*m for _ in range(n)]

    for _ in range(k):
        x, y = map(int, input().split())
        graph[y][x] = 1
    
    
    visited = [[False]*m for _ in range(n)]
    ans = 0
    for i in range(n):
        for j in range(m):
            if not visited[i][j] and graph[i][j] == 1:
                bfs(graph, visited, i, j, n, m)
                ans += 1
    
    print(ans)