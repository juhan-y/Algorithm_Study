import sys
from collections import deque

M, N = map(int, sys.stdin.readline().split())
to = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
dq = deque()
cnt = 0
dx = [-1, 0, 1, 0] # 북동남서
dy = [0, 1, 0, -1] # 북동남서

# 현재 토마토가 있는 좌표 deque에 추가
for i in range(N) :
    for j in range(M) :
        if to[i][j] == 1 :
            dq.append([i, j])

def findto() : # BFS
    while dq :
        x, y = dq.popleft()
        for i in range(4) : # 북동남서의 4방향 탐색
            nx, ny = x + dx[i], y + dy[i]
            if (0 <= nx < N) and (0 <= ny < M) and to[nx][ny] == 0 :
                to[nx][ny] = to[x][y] + 1 # 날짜의 누적합
                # 0 1 0        2 1 2        2 1 2        2 1 2
                # 0 0 0   ->   0 2 0   ->   3 2 3   ->   3 2 3
                # 0 0 0        0 0 0        0 3 0        4 3 4
                dq.append([nx, ny]) # 토마토가 익은 상태 deque에 삽입

findto()

cnt = max(map(max, to)) - 1 # 이중리스트에서 전체 최대값 찾기 위한 map 이용
for t in to :
    if 0 in t :
        cnt = -1
print(cnt)