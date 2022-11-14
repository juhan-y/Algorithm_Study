from collections import deque
n, m = map(int, input().split())
graph = []
for _ in range(n):
    ls = input()
    temp = []
    for i in ls:
        temp.append(int(i))
    graph.append(temp)

di = [0,1,0,-1]
dj = [1,0,-1,0]

def bfs(i, j):
    q = deque()
    q.append((i,j))
    while q:
        ci, cj = q.popleft()
        for k in range(4):
            ni = ci + di[k]
            nj = cj + dj[k]
            if 0 <= ni < n and 0 <= nj < m and graph[ni][nj] == 0:
                graph[ni][nj] = 1
                q.append((ni, nj))
    
cnt = 0
for i in range(n):
    for j in range(m):
        if graph[i][j] == 0:
            bfs(i, j)
            cnt += 1
print(cnt)