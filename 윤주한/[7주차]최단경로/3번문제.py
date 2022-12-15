INF = int(1e9)
n = int(input())
m = int(input())

distance = [[INF] * (n+1) for _ in range(n+1)]

for i in range(n+1):
    distance[i][i] = 0
for _ in range(m):
    a, b, c = map(int, input().split())
    distance[a][b] = c

for i in range(1, n+1):
    for j in range(1, n+1):
        for k in range(1, n+1):
            distance[i][j] = min(distance[i][j], distance[i][k]+distance[k][j])
    
for i in range(1, n+1):
    for j in range(1, n+1):
        print(distance[i][j], end=' ')
    print()