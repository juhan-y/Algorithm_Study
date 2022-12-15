"""
개선된 다익스트라 알고리즘은 힙 구조를 사용하여 출발노드로부터 가장 거리가 짧은 노드를 더욱 빠르게 찾을 수 있다.
 > 우선순위 큐는 가장 우선순위가 높은 데이터부터 추출된다.(가장 먼저 삽입된 데이터 출력 x)
 > 최소힙 : 값이 낮은 데이터가 먼저 출력
 > 최대힙 : 값이 높은 데이터가 먼저 출력
 > 현재 가장 가까운 노드를 저장하기 위한 목적으로만 우선순위 큐를 추가로 이용

 우선순위 큐를 이용할때 :
    기본적으로 거리가 짧은 원소가 우선순위 큐의 최상위 원소로 위치해있기 때문에 큐에서 노드를 꺼낸 뒤 해당 노드를 이미 처리한 적이
    있다면 무시하고 아직 처리하지 않았다면 처리하면 된다.
"""

import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

n, m = map(int, input().split())
start = int(input())
graph = [[]for i in range(n+1)]
distance = [INF]*(n+1)

for _ in range(m):
    a,b,c = map(int, input().split())

    graph[a].append((b,c))

def dijkstra(start) :
    q = []
    heapq.heappush(q, (0,start)) #시작노드로 가기위한 비용은 0
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)

        if distance[now] <dist:
            continue
        
        for i in graph[now] :
            cost = dist+i[1]
            if cost < distance[i[0]] :
                distance[i[0]] = cost
                heapq.heappush(q,(cost,i[0]))

dijkstra(start)

for i in range(1, n+1) :
    if distance[i] == INF :
        print('INFINITY')
    else :
        print(distance[i])