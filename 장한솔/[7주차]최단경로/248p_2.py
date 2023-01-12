import heapq
import sys
INF = int(1e9)

n, m = map(int, sys.stdin.readline().split())
start = int(sys.stdin.readline())

graph = [[] for _ in range(n+1)]
distance = [INF] * (n+1)
# heapq 이용 방식은 visited 필요 없음!

for i in range(m) :
    a, b, c = map(int, sys.stdin.readline().split())
    graph[a].append((b, c))
    
def di(start) :
    q = []
    heapq.heappush(q, (0, start)) # heapq에 시작노드로 가기 위한 최단경로는 0으로 설정해서 넣음 (default 값 설정)
    distance[start] = 0
    
    while q : # q가 empty 상태가 아니라면,
        d, now = heapq.heappop(q) # 최단경로 꺼내기
        
        if (distance[now] < d) : # 현재 설정된 최단경로보다 짧은 최단경로 : 이미 방문했던노드 라면 무시하기
            continue
        
        for i in graph[now] :
            cost = d + i[1]
            if cost < distance[i[0]] : # 지금 계산한 비용이 최소비용이라면 갱신하기
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))
                
di(start)

for i in range(1, n+1) :
    if distance[i] == INF :
        print("INFINITY")
    else :
        print(distance[i])
        