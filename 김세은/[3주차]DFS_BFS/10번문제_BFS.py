#10번문제_BFS
from collections import deque

N, M = map(int, input().split())
graph = []
for i in range(N):
    a = list(map(int, input()))
    graph.append(a)

# 상하좌우 방향
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    if graph[x][y] == 0:
        queue = deque()
        queue.append((x,y))

        # 방문 지점 표시
        graph[x][y] = 1

        # 큐가 빌 때까지 반복, 없어지면 1추가 후 break
        while True:
            if not queue:
                return 1
            
            x, y = queue.popleft()

            # 현재 위치에서 네 방향으로의 위치 확인
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                # 주어진 공간을 벗어나면 무시
                if nx<0 or ny<0 or nx>=N or ny>=M:
                    continue

                # 1인 경우 칸막이이므로 무시
                if graph[nx][ny] == 1:
                    continue

                # 0인 경우 구멍이 뚫린 부분이므로 큐에 추가
                if graph[nx][ny] == 0:
                    queue.append((nx, ny))
                    # 방문 지점 1로 표시
                    graph[nx][ny] = 1
        
    return 0

count = 0
for x in range(N):
    for y in range(M):
        count += bfs(x, y)

print(count)
