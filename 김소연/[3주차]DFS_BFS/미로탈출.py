# 최단경로 찾기 -> bfs
import sys
from collections import deque

n,m = map(int, input().split())

g = []
for i in range(n):
    g.append(list(map(int, input())))

# 북동남서
dx = [-1,0,1,0]
dy = [0,1,0,-1]
    
count = 0

def bfs(x, y):
    q = deque()
    q.append((x,y))
    
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if (nx<0 or ny <0 or nx >= n or ny >= m):
                continue
            if g[nx][ny] == 0: 
                continue
            if g[nx][ny] == 1:
                g[nx][ny] = g[x][y] + 1
                q.append((nx, ny))
                
    return g[n-1][m-1]

print(bfs(0,0))

