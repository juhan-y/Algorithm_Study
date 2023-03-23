# 플로이드 워셜 알고리즘 
# 시간복잡도 O(N^3)

INF = int(1e9)

n = int(input())
m = int(input())
graph = [[INF]*(n+1) for _ in range(n+1)] # 2차원 리스트

# 자기자신에서 자기자신으로 가는 비용은 0으로 초기화
for a in range(1, n+1):
    for b in range(1, n+1):
        if a==b:
            graph[a][b] = 0

for _ in range(m):
    a, b, c = map(int, input().split()) # a에서 b로 가는 비용 c 
    graph[a][b] = c

# 3중 for문
for k in range(1,n+1):
    for a in range(1,n+1):
        for b in range(1,n+1):
            graph[a][b] = min(graph[a][b], graph[a][k]+graph[k][b])

for a in range(1,n+1):
    for b in range(1,n+1):
        if graph[a][b] == INF:
            print("INFINITY", end=" ")
        else:
            print(graph[a][b],end=" ")
    print()