import sys
INF = int(1e9)

N, M = map(int, sys.stdin.readline().split())
distance = [[INF] * (N+1) for _ in range(N+1)]

for i in range(1, N+1) :
    for j in range(1, N+1) :
        if i == j :
            distance[i][j] = 0
        
for _ in range(M) :
    a, b = map(int, sys.stdin.readline().split())
    distance[a][b] = 1
    distance[b][a] = 1 
    
x, k = map(int, sys.stdin.readline().split())

for i in range(1, N+1) :
    for a in range(1, N+1) :
        for b in range(1, N+1) :
            distance[a][b] = min(distance[a][b], distance[a][i] + distance[i][b])
            
dis = distance[1][k] + distance[k][x]

if dis >= INF :
    print("-1")
else :
    print(dis)