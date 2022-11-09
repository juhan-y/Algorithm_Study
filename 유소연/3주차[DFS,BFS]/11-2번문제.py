from collections import deque
import sys

N, M = map(int, sys.stdin.readline().split())

arr = []

dx = [-1,0,1,0]
dy = [0,-1,0,1]

for i in range(N) :
    temp = list(map(int, input()))
    arr.append(temp)

def bfs(x, y) :
    que = deque() 

    que.append((x,y)) # que에 시작위치를 입력

    while que : # que가 비어있을때까지 반복
        x, y = que.popleft() # que에 가장 먼저 들어간 x,y를 꺼낸다

        for i in range(4) : # 꺼낸 x,y의 상하좌우 검사를 위함
            temp0 = x+dx[i]
            temp1 = y+dy[i]

            # 1. 해당 방의 위치가 조건에 맞지 않으면 continue(0보다 작거나, N,M보다 크거나)
            if temp0<0 or temp1<0 or temp0>=N or temp1>=M :
                continue
            # 2. 해당 방의 값이 0이라 갈 수 없는 곳이면 continue
            if arr[temp0][temp1] == 0 :
                continue
            #3. 해당 방의 값이 1이면 해당 방을 이전 x,y의 방의 값 +1을 하여 거리정보를 저장
            if arr[temp0][temp1] == 1 :
                arr[temp0][temp1] = arr[x][y] +1

                #4. 해당 방을 다음 경로로 지정하기 위하여 que에 저장한다.

                que.append((temp0, temp1))

    #5. while이 끝났다는것은 더이상 que에 data가 존재하지 않는다는 것 이므로 bfs를 종료시킨다. 이때 우리가 찾고싶은 방은 N,M이므로 배열의 INDEX를 고려하여 -1한 값을 찾는다.
    return arr[N-1][M-1]

print(bfs(0,0))