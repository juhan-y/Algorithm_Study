import sys

N, M = map(int, sys.stdin.readline().split())
arr = []
count = 0
for i in range(N) :
    temp = list(map(int, input()))
    arr.append(temp)

def dfs(x,y) :
    if x<=-1 or x>=N or y<=-1 or y>=M :
        return False
    if arr[x][y] == 0:
        arr[x][y] == 1

        dfs(x-1,y)
        dfs(x,y-1)
        dfs(x+1,y)
        dfs(x,y+1)
        return True
    return False

for i in range(N) :
    for j in range(M) :
        if dfs(i,j)==True:
            count+=1

print(count)