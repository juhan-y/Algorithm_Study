import sys

n, m = map(int, input().split())
x, y, d = map(int, input().split())

dir = [0, 1, 2, 3] 
# 북 동 남 서
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


gmap = []
cnt = 1
for i in range(n):
    gmap.append(list(map(int, input().split())))

gmap[x][y] = 1

# 반시계 방향
idx = dir.index(d)
    
while(1):
    
    # 반시계 방향
    idx -= 1

    if idx == -1:
        idx = 3
    
    nx = x + dx[idx]
    ny = y + dy[idx]

    if gmap[nx][ny] == 0:
        x = nx
        y = ny
        gmap[nx][ny] = 1
        cnt += 1
    
    count_n = 0
    for i in gmap:
        if 0 not in i:
            count_n += 1
    if count_n == n:
        break

print(cnt)