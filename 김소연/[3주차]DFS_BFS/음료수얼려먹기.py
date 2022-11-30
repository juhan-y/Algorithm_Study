import sys
# 그룹으로 묶기 -> dfs

n,m = map(int, input().split())
graph = []

for _ in range(n):
    graph.append(list(map(int, input())))
    
def dfs(x,y):
    global graph
    
    #현재 노드 방문
    graph[x][y] = 1
    
    # 북동남서
    dx = [-1,0,1,0]
    dy = [0,1,0,-1]
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        
        #얼음판 내부인지 확인
        if (nx >= 0 and nx < n and ny >= 0 and ny < m):

            #얼음 틀 = 0, 벽 = 1
            if graph[nx][ny] == 0:
                dfs(nx, ny)

    
result = 0
for i in range(n):
    for j in range(m):
        if graph[i][j] == 0:
            dfs(i, j)
            result += 1
            
print(result)
            
        
        
        