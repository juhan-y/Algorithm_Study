import sys

#반시계: 북서남동
dx = [0, -1, 0, 1]
dy = [-1, 0, 1, 0]

n, m = map(int, input().split())
gmap = [[0] * m for _ in range(n)]

x, y, dir = map(int, input().split())

array = []
for i in range(n):
    array.append(list(map(int, input().split())))
    

#현재 위치 방문 =1처리
gmap[x][y] = 1
#현재위치 방문해서 cnt 1
cnt = 1
turn_cnt = 0

while True:
    #현재 위치에서 왼쪽 방향
    # 0, 1, 2, 3 순환 (dx,dy 인덱스)
    dir -= 1
    if dir == -1: dir = 3
    
    nx = x + dx[dir]
    ny = y + dy[dir]
    
    #왼회전한 곳에 안가본 곳 존재하는 경우 이동
    if gmap[nx][ny] == 0 and array[nx][ny] ==0:
        gmap[nx][ny] = 1
        x = nx
        y = ny
        cnt +=1
        # 있으면 회전 안하고 전진
        turn_cnt = 0
        continue
    
    else:
        turn_cnt +=1
    
    # 4방향 모두 이동 불가 -> 후진
    if turn_cnt == 4:
        nx = x - dx[dir]
        ny = y - dy[dir]
        # 이동 가능
        if array[nx][ny] == 0:
            x = nx
            y = ny
        # 이동 불가능
        else:
            break
        turn_cnt = 0
        
print(cnt)
            
        
        