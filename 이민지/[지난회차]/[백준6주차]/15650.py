# 방법 1
from itertools import combinations
n,m = map(int,input().split())
l = list(range(1,n+1))
for i in combinations(l,m):
    for j in i:
        print(j,end=' ')
    print()


# 방법 2
n, m = list(map(int,input().split()))
s = []

def dfs(start):
    if len(s)==m:
        print(' '.join(map(str, s)))
        return
    
    for i in range(start, n+1):
        s.append(i)
        dfs(i+1)
        s.pop()
            
dfs(1)