import sys
sys.setrecursionlimit(10 ** 6) # 재귀이용문제에서 runtimeerror 방지하는 코드

N, M = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(N+1)] # 정점 개수대로 그래프 만들기
visited = [0] * (N+1) # 정점 개수대로 방문리스트 만들기
cnt = 0

for _ in range(M) : # 간선 개수대로 입력받아 graph에 저장
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

def com(v) :
    visited[v] = 1
    for i in graph[v] :
        if visited[i] == 0 :
            com(i)

for i in range(1, N+1) : # 정점 다 for문에서 돌 수 있도록
    if visited[i] == 0 : # 방문하지 않은 노드만
        com(i)  # com 함수 돌고
        cnt += 1 # cnt +1

print(cnt)