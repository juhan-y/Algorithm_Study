from collections import deque
n, m = map(int, input().split())

di = [0,1,0,-1]
dj = [1,0,-1,0]

graph = []
for _ in range(m):
    graph.append(list(map(int, input().split())))


riped = []
for i in range(m):
    for j in range(n):
        if graph[i][j] == 1:
            riped.append((i, j))

q = deque()
for i in riped:
    q.append(i)
    
while q:
    i, j = q.popleft()
    for k in range(4):
        ni = i + di[k]
        nj = j + dj[k]
        if 0 <= ni < m and 0 <= nj < n:
            if graph[i][j] + 1 < graph[ni][nj] or graph[ni][nj] == 0:
                graph[ni][nj] = graph[i][j] + 1
                q.append((ni,nj))

no_ripe = False
for i in range(m):
    if graph[i].count(0) > 0:
        no_ripe = True
        break
if no_ripe == True:
    print(-1)
else:
    max_date = 0
    for i in range(m):
        max_date = max(max(graph[i]), max_date)
    print(max_date - 1)