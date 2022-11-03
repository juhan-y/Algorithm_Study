import sys

n, m = map(int, input().split())
x, y, d = map(int, input().split())

# 반시계 :북서남동
dir = [0, 3, 2, 1] 
dx = [0, -1, 0, 1]
dy = [-1, 0, 1, 0]

gmap = []
cnt = 1
for i in range(n):
    gmap.append(list(map(int, input().split())))

idx = dir.index(d)+1
while(1):
    gmap[x][y] = 1
    nx = x + dx[idx]
    ny = y + dy[idx]

    if gmap[nx][ny] == 0:
        x = nx
        y = ny
        gmap[nx][ny] = 1
        cnt += 1

    if idx < 3:
        idx += 1
    else:
        idx = 0
    
    count_n = 0
    for i in gmap:
        if 0 not in i:
            count_n += 1
    if count_n == n:
        break

print(cnt)