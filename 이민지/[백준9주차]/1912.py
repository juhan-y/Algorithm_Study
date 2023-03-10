import sys
input = sys.stdin.readline
n = int(input())
d = list(map(int,input().split()))
for i in range(1,n):
    d[i] += max(d[i-1],0)
print(max(d))