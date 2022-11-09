from collections import deque
import sys

N, M = map(int, sys.stdin.readline().split())

arr = []

dx = [-1,0,1,0]
dy = [0,-1,0,1]

for i in range(N) :
    temp = list(map(int, input()))
    arr.append(temp)

def bfs(x,y) :
    que = deque()

    que.append((x,y))

    while que :
        x, y = que.popleft()

        for i in range(4) :
            temp0 = x + dx[i]
            temp1 = y + dy[i]

            if temp0 <0 or temp1 <0 or temp0>=N or temp1>=M :
                continue
            if arr[temp0][temp1] == 0 :
                continue
            if arr[temp0][temp1] ==1 :
                arr[temp0][temp1] = arr[x][y]+1

                que.append((temp0,temp1))
    
    return arr[N-1][M-1]

print(bfs(0,0))