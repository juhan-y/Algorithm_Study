import heapq
t = int(input())

di = [1, 0, -1, 0]
dj = [0, 1, 0, -1]

def bfs(x, y, graph, n, m):
    q = []
    heapq.heappush(q, (x, y))
    graph[y][x] = 0
    while q:
        j, i = heapq.heappop(q)
        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            if 0 <= ni < n and 0 <= nj < m:
                if graph[ni][nj] == 1:
                    graph[ni][nj] = 0
                    heapq.heappush(q, (nj, ni))


for _ in range(t):
    m, n, k = map(int, input().split())
    graph = [[0] * m for _ in range(n)]
    for _ in range(k):
        a, b = map(int, input().split())
        graph[b][a] = 1

    cnt = 0
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 1:
                bfs(j, i, graph, n, m)
                cnt += 1
        
    print(cnt)