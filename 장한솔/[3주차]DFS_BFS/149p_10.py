import sys

N, M = map(int, sys.stdin.readline().split())

graph = []
for i in range(N) :
    graph.append(list(map(int, sys.stdin.readline().strip())))

def DFS(x, y):
    if (x < 0) or (x >= N) or (y < 0) or (y >= M):
        return False

    if graph[x][y] == 0:
        graph[x][y] = 1

        DFS(x - 1, y)  # 현재노드 왼쪽
        DFS(x, y - 1)  # 현재노드 아래쪽
        DFS(x + 1, y)  # 현재노드 오른쪽
        DFS(x, y + 1)  # 현재노드 위쪽
        return True

    return False


result = 0
for i in range(N):
    for j in range(M):
        if DFS(i, j) == True:
            result += 1

print(result)