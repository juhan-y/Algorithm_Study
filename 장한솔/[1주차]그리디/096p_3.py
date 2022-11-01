import sys

N, M = map(int, sys.stdin.readline().split())

min_num = 0
for i in range(N) :
    li = list(map(int, sys.stdin.readline().split()))
    li.sort()
    
    if min_num < li[0] :
        min_num = li[0]
    
print(min_num)