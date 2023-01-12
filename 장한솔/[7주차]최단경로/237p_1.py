import sys
INF = int(1e9)

n, m = map(int, sys.stdin.readline().split()) # n: 노드개수 / m: 간선개수
start = int(sys.stdin.readline()) # 시작노드

graph = [[] for _ in range(n+1)] # 연결된 리스트 만들기 위함
visited = [0] * (n+1)  # 방문여부 리스트 생성

distance = [INF] * (n+1) # 최단거리리스트 무한으로 초기화!

for _ in range(m) :
    a, b, c = map(int, sys.stdin.readline().split())
    graph[a].append((b, c)) # 튜플형태로 도착지, 비용 저장
    
def min_node() :
    min_val = INF
    index = 0 # 최단거리 짧은 인덱스 저장, default값 0으로 지정
    for i in range(1, n+1) : # 0은 default 값이기 때문에 1부터 for문 돌면 됨
        if (distance[i] < min_val) and not visited[i] : # 방문하지 않았고, min_val보다 작으면 if문 조건 충족
            min_val = distance[i]
            index = i
    return index

def di(start) :
    distance[start] = 0
    visited[start] = 1
    for i in graph[start] : # start 노드와 연결된 모든 노드들에 대해 작업 (i는 현재 튜플상태)
        distance[i[0]] = i[1] # distance[i[0]] : distance 테이블의 i[0](노드정보) 칸에 i[1](해당 노드의 비용) 입력
        
    for i in range(n-1) :
        now = min_node()
        visited[now] = 1
        
        for i in graph[now] :
            cost = distance[now] + i[1]
            if cost < distance[i[0]] : # 기존 저장된 거리비용보다 지금 계산한 거리비용이 낮으면 교체
                distance[i[0]] = cost

di(start)

for i in range(1, n+1) :
    if distance[i] == INF :
        print("INFINITY")
    else :
        print(distance[i])