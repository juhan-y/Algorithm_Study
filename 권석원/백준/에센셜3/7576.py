import sys
from collections import deque

M,N = map(int,sys.stdin.readline().split())

map_list = []
q = deque()

dx = [0,0,-1,1]
dy = [-1,1,0,0]
day_list = [[0] * M for _ in range(N)]

for i in range(N):
    input_list = list(map(int,sys.stdin.readline().split()))

    for j in range(M):
        if input_list[j] == 1:
            q.append((i,j))
        
        if input_list[j] == 0:
            day_list[i][j] = -1

    map_list.append(input_list)



ans = 0

while q:
    y,x = q.popleft()

    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]

        if nx < 0 or nx >= M: continue
        if ny < 0 or ny >= N: continue
        if map_list[ny][nx] == -1 : continue
        if day_list[ny][nx] > -1 :continue

        day_list[ny][nx] = day_list[y][x] + 1
        
        q.append((ny,nx))


flag = True
for tomato_list in day_list:
    for tomato in tomato_list:
        if tomato == -1:
            print(-1)
            flag = False
            break
        else:
            ans = max(ans,tomato)
    
    if flag == False:
        break

if flag:
    print(ans)