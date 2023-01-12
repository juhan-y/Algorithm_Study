# 비슷하게 풀었는데 모르겠어요 ㅠ

import sys

N,M = map(int,sys.stdin.readline().rstrip().split())

a,b,d = map(int,sys.stdin.readline().rstrip().split())

map_list = []

for i in N:
    lst = list(map(int,sys.stdin.readline().rstrip().split()))
    map_list.append(lst)
    
map_list[a][b] = 2

def direction(d):
    if d == 0:
        return 3
    else :
        return d-1
    
def reverse_direction(d):
    if d == 0:
        return 2
    elif d == 1 :
        return 3
    elif d == 2 :
        return 0
    else :
        return 1
    
D = direction(d)

dx = [0,1,0,-1]
dy = [-1,0,1,0]
cnt = 0

while True:
    nx = b + dx[D]
    ny = a + dy[D]
    
    if D != d:
    
        if nx < 0 and nx >= M : 
            D = direction(D)
            continue
        
        if ny < 0 and ny >= N :
            D = direction(D)
            continue
        
        if map_list[ny][nx] == 0:
            cnt += 1
            map_list[ny][nx] = 1
            tmp_d = direction(D)
            
            tmp_x = nx + dx[tmp_d]
            tmp_y = ny + dy[tmp_d]
            
            if map_list[tmp_y][tmp_x] == 1:
                D = direction(D)
    else:
        if (nx < 0 and nx >= M) or (ny < 0 and ny >= N): 
            D = reverse_direction(D)
            
            
            
            if map_list[ny][nx] == 0:
                cnt += 1
                map_list[ny][nx] = 1
                tmp_d = direction(D)
                
                tmp_x = nx + dx[tmp_d]
                tmp_y = ny + dy[tmp_d]
        
            

    
    

