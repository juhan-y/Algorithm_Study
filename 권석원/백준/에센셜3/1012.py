import sys
from collections import deque

T = int(sys.stdin.readline())

dx = [0,0,1,-1]
dy = [1,-1,0,0]

for _ in range(T):
    M, N, K = map(int, sys.stdin.readline().split())

    graph = [ [0] * M for _ in range(N) ]
    q_first = deque()

    for _ in range(K):
        x,y = map(int, sys.stdin.readline().split())
        graph[y][x] = 1
        q_first.append([y,x])
    
    
    q = deque()
    cnt = 0

    while q_first:
            i,j = q_first.popleft()

            if graph[i][j]:
                cnt += 1
                
                q.append([i,j])
                graph[i][j] = 0
                while q:
                    y,x = q.popleft()      
                    

                    for k in range(4):
                        nx = x + dx[k]
                        ny = y + dy[k]

                        if nx < 0 or nx >= M: continue
                        if ny < 0 or ny >= N: continue

                        if graph[ny][nx]:
                            q.append([ny,nx])
                            graph[ny][nx] = 0
    
    print(cnt)

