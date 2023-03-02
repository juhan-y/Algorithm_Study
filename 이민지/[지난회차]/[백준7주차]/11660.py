import sys
input = sys.stdin.readline

n,m = map(int,input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
summ = [[0]*(n+1) for _ in range(n+1)]
for i in range(n+1):
    for j in range(n+1):
        summ[i][j] = summ[i][j-1] + summ[i-1][j] - summ[i-1][j-1] + arr[i-1][j-1] 

for _ in range(m):
    x1,y1,x2,y2 = map(int,input().split())
    print(summ[x2][y2] - summ[x1-1][y2] - summ[x2][y1-1] + summ[x1-1][y1-1])
        

