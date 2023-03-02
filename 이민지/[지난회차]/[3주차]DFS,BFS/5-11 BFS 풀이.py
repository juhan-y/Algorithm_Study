from collections import deque

n, m = map(int, input().split())
my_list = []
for i in range(n):
    my_list.append(list(map(int, input())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x,y):
    q = deque()
    q.append((x,y))
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            if my_list[nx][ny] == 1:
                my_list[nx][ny] += my_list[x][y]
                q.append((nx, ny)) 
    return my_list[n-1][m-1]

print(bfs(0,0))

