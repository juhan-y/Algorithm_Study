# DFS 구현
def DFS(graph, v, visited) :
    visited[v] = True # 현재 노드 방문 처리
    print(v, end = ' ') # 출력
    
    for i in graph[v] : # 현재 노드와 연결된 다른 노드 재귀적 방문
        if not visited[i] :
            DFS(graph, i, visited)

graph = [
    [], # 0번 노드의 인접노드
    [2, 3, 8], # 1번 노드의 인접노드
    [1, 7], # 2번 노드의 인접노드
    [1, 4, 5], # 3번 노드의 인접노드
    [3, 5], # 4번 노드의 인접노드
    [3, 4], # 5번 노드의 인접노드
    [7], # 6번 노드의 인접노드
    [2, 6, 8], # 7번 노드의 인접노드
    [1, 7] # 8번 노드의 인접노드
]

visited = [False] * 9 

# DFS(graph, 1, visited) # 노드 1을 시작노드로 지정 1 2 7 6 8 3 4 5 출력
DFS(graph, 3, visited) # 노드 3을 시작노드로 지정 3 1 2 7 6 8 4 5 출력
