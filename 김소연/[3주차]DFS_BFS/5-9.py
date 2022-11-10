# bfs
import sys
from collections import deque

g = [[],
         [2,3,8],
         [1,7],
         [1,4,5],
         [3,5],
         [3,4],
         [7],
         [2,6,8],
         [1,7]]

visited = [False] * 9

def bfs(g, start, visited):
    queue = deque([start])
    visited[start] = True
    
    while queue:
        v = queue.popleft()
        print(v, end = ' ')
        for i in g[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
                
bfs(g,1,visited)
            