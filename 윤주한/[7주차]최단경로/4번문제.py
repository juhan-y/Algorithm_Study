n, m = map(int, input().split())

INF = int(1e9)

distance = [[INF] * (n+1) for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    distance[a][b] = 1
    distance[b][a] = 1

x, k = map(int, input().split())

for i in range(1, n+1):
    for j in range(1, n+1):
        for k in range(1, n+1):
            distance[i][j] = min(distance[i][j], distance[i][k]+distance[k][j])

if distance[1][k] + distance[k][x] >= INF:
    print(-1)
else:
    print(distance[1][k] + distance[k][x])