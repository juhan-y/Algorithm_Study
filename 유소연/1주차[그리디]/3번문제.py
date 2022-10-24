import sys

n, m = map(int, sys.stdin.readline().split())
num = 0
for i in range(n) :
    arr = list(map(int, sys.stdin.readline().split()))
    if min(arr)>num : 
        num = min(arr)
print(num)