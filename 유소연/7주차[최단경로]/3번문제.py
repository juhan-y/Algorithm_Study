"""
플로이드 워셜 알고리즘
    모든 지점에서 다른 모든 지점까지의 최단 경로를 모두 구해야 하는 경우 사용하는 알고리즘
    Dab = min(Dab, Dak + Dkb) # a에서 b까지 갈 때, k를 거쳐가는것과 직접가는것중 최소값을 찾는다.
"""
import sys
input = sys.stdin.readline
INF = (1e9)

n = int(input())
m = int(input())
graph = [[INF]*(n+1) for _ in range(m+1)]

for a in range(1, n+1) : # 자기 자신은 0으로 초기화 
    for b in range(1, n+1) :
        if a==b :
            graph[a][b] = 0

for _ in range(m) :
    a,b,c = map(int, input().split())
    graph[a][b] = c

for k in range(1, n+1) :
    for a in range(1, n+1) :
        for b in range(1, n+1) :
            graph[a][b] = min(graph[a][b], graph[a][k]+graph[k][b])

for a in range(1, n+1) :
    for b in range(1, n+1) :
        if graph[a][b] == INF :
            print('INF',end=' ')
        else :
            print(graph[a][b], end=' ')

    print()