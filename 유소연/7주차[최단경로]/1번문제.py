import sys

input = sys.stdin.readline
INF = int(1e9)

n, m = map(int, input().split())

start = int(input())
graph = [[] for i in range(n+1)]
visited = [False]*(n+1) #방문했는지 체크하는 배열
distance = [INF]*(n+1) # 거리를 저장하는 배열

for _ in range(m) :
    a,b,c = map(int, input().split()) # a노드에서 b노드로 가는 비용 c
    graph[a].append((b, c))

def get_smallest_node() :
    min_value = INF
    index = 0

    for i in range(1, n+1) :
        if distance[i] < min_value and not visited[i] : # distance[i]가 min value보다 작고 방문하지 않은 노드라면
            min_value = distance[i]
            index = i
    return index

def dijkstra(start) :
    distance[start] = 0
    visited[start] = True # 시작노드의 거리를 0으로 초기화, 방문했다고 표시

    for j in graph[start] :
        distance[j[0]] = j[1]

    for i in range(n-1) :
        now = get_smallest_node()
        visited[now] = True

        for j in graph[now] :
            cost = distance[now] + j[1]

            if cost<distance[j[0]]:
                distance[j[0]] = cost

dijkstra(start)

for i in range(1, n+1) :
    if distance[i] == INF :
        print('INFINITY')
    else :
        print(distance[i])
 