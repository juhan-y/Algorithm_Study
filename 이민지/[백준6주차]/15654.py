# 방법 1
from itertools import permutations
n,m=map(int,input().split())
l = list(map(int, input().split()))
ans = []
for i in permutations(l,m):
    ans.append(i)
ans.sort()
for i in ans:
    for j in i:
        print(j,end=' ')
    print()

# 방법 2
n, m = list(map(int,input().split()))
l = sorted(list(map(int,input().split())))
s = []

def dfs():
    if len(s)==m:
        for j in s:
            print(l[j], end=' ')
        print()
        return 
    
    for i in range(0, n):
        if i in s:
            continue
        s.append(i)
        dfs()
        s.pop()
            
dfs()