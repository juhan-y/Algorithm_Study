import sys
INF = int(1e9)

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())

distance = [[INF] * (n+1) for _ in range(n+1)]

# 나에게서 나에게로.. 0 처리
for i in range(1, n+1) :
    for j in range(1, n+1) :
        if i == j :
            distance[i][j] = 0
            
# 입력받아서 저장 (2차원 배열 형태 저장)
for _ in range(m) :
    a, b, c = map(int, sys.stdin.readline().split())
    distance[a][b] = c
    
# 점화식 기반 최단거리 계산
for k in range(1, n+1) :
    for l in range(1, n+1) :
        for h in range(1, n+1) :
            distance[l][h] = min(distance[l][h], distance[l][k] + distance[k][h])

# 출력
for j in range(1, n+1) :
    for i in range(1, n+1) :
        if distance[j][i] == INF :
            print('INFINITY')
        else :
            print(distance[j][i], end = " ")
    print()
    
