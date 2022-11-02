import sys

dx = [0,0,1,-1]
dy = [1,-1,0,0]

dic = {'R':2,
       'U':1,
       'D':0,
       'L':3}


N = int(sys.stdin.readline())

mv_list = sys.stdin.readline().rstrip().split()

x, y = 1, 1

for mv in mv_list:
    k = dic[mv]
    
    nx = x + dx[k]
    ny = y + dy[k]
    
    if nx < 1 or nx >= N : continue
    if ny < 1 or ny >= N : continue
    
    x,y = nx, ny
    
print(y,x)