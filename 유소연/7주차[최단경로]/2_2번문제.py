import heapq
import sys

input = sys.stdin.readline
INF = (1e9)

n, m = map(int, input().split())
start = int(input())
graph = [[] for i in range(n+1)]
distance = [INF]*(n+1)

for _ in range(m) :
    a,b,c = map(int, input().split())
    graph[a].append((b,c)) #a노드에서 b노드까지 가는데 걸리는 시간 

def dijkstra(start) :
    q = []
    heapq.heappush(q, (0, start)) #q에서는 튜플의 0번 값을 가지고 정렬을 해서 앞쪽에 거리를 넣는듯?
    distance[start] = 0 #시작지점부터 시작지점까지의 거리는 0이기때문에 0으로 초기화

    while q :
        dist, now = heapq.heappop(q) #q에서 거리와 현재 노드 출력

        if distance[now] < dist :
            continue

        for i in graph[now] : #graph에 저장한 현재 노드와 연결된 다른 노드의 정보 출력
            cost = dist+i[1] # dist와 더하는 이유는 현재 노드를 거쳐가는게 더 빠른지 아닌지 확인하기 위함인가

            if cost < distance[i[0]] :
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

dijkstra(start)

for i in range(1, n+1) :
    if i==INF :
        print('INF')
    else :
        print(distance[i])

