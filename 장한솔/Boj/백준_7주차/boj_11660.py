import sys

N, M = map(int, sys.stdin.readline().split())

graph = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
s = [[0 for _ in range(N+1)] for _ in range(N+1)] # 누적합 계산 위함

for i in range(1, N+1) :
    for j in range(1, N+1) :
        s[i][j] = (s[i-1][j] + s[i][j-1] - s[i-1][j-1]) + graph[i-1][j-1]

for _ in range(M) :
    x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
    answer = s[x2][y2] - s[x1-1][y2] - s[x2][y1-1] + s[x1-1][y1-1]
    print(answer)