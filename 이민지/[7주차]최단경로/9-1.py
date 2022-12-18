# 간단한 다익스트라 알고리즘
# 시간복잡도 O(V^2), V는 노드 개수

import sys
input = sys.stdin.readline
INF = int(1e9) 

n, m = map(int, input().split()) # 노드 개수, 간선 개수 입력
start = int(input()) # 시작노드 입력
graph = [[] for i in range(n+1)] # 노드 정보 리스트, 인덱스 번호와 맞추기 위해 크기는 n+1로
visited = [False] * (n+1) # 방문 기록
distance = [INF] * (n+1) # 최단거리 기록

for _ in range(m):
    a, b, c = map(int, input().split()) # a번 노드에서 b번 노드로 가는 비용이 c
    graph[a].append((b,c))

def get_smallest_node():
    min_value = INF
    index = 0
    for i in range(1, n+1):
        if distance[i] < min_value and not visited[i]:
            min_value = distance[i]
            index = i
    return index

def dijkstra(start):
    distance[start] = 0
    visited[start] = True
    for j in graph[start]:
        distance[j[0]] = j[1] # j[0]은 시작 노드와 연결된 노드 번호, j[1]은 그 노드로 가는 비용
    for i in range(n-1):
        now = get_smallest_node()
        visited[now] = True
        for j in graph[now]:
            cost = distance[now] + j[1]
            if cost < distance[j[0]]:
                distance[j[0]] = cost

dijkstra(start)

for i in range(1, n+1):
    if distance[i] == INF:
        print("INFINITY")
    else:
        print(distance[i])