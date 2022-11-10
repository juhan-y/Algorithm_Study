# 인접리스트 방식 예제
graph = [[] for _ in range(3)] # _ : 반복을 수행하되, 반복을 위한 변수의 값 무시할 때

graph[0].append((1, 7)) # (노드, 간선)
graph[0].append((2, 5))

graph[1].append((0, 7))

graph[2].append((0, 5))

print(graph)