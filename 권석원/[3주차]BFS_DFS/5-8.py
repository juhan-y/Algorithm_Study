from collections import deque

stack = deque([1])

graph = [[] for _ in range(9)]

graph[1] = [2,3,8]
graph[2] = [1,7]
graph[3] = [1,4,5]
graph[4] = [3,5]
graph[5] = [3,4]
graph[6] = [7]
graph[7] = [2,6,8]
graph[8] = [1,7]

visited = []

while stack:
    k = stack.pop()
    visited.append(node)
    
    for node in graph[k]:
        if node not in visited:      
            stack.append(node)
    
    