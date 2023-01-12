import sys
from itertools import *

num_node = int(sys.stdin.readline())

cnt = int(sys.stdin.readline())
INF = int(1e9)

graph = [ [] for _ in range(num_node+1) ]
graph_w = [ [INF]*(num_node+1) for _ in range(num_node+1) ]

for i in range(cnt):
    st,ed,w = map(int,sys.stdin.readline().split())
    graph[st].append(ed)
    graph[st].sort()
    graph_w[st][ed] = w

for i in range(1,num_node+1):  
    graph_w[i][i] = 0
     
for i in range(1,num_node+1):  
    
    to_node = graph[i].copy()
    
    from_node = []
    
    for j in range(1,num_node+1):  
        if j != i : 
            if i in graph[j]:
                from_node.append(j)
    
    nPr = list(set(list(permutations(to_node + from_node,2))))
    
    for to_from in nPr:
        start,end = to_from
        
        graph_w[start][end] = min(graph_w[start][end],graph_w[i][end] + graph_w[start][i])
        
        
for i in range(1,num_node+1):
    print(graph_w[i])

    
# 4
# 7
# 1 2 4
# 1 4 6
# 2 1 3
# 2 3 7
# 3 1 5
# 3 4 4
# 4 3 2
