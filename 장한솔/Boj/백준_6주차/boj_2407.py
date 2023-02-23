import sys

n, m = map(int, sys.stdin.readline().split())

bj = 1
for i in range(n, n-m, -1) :
    bj = bj * i
bm = 1
for i in range(1, m+1) :
    bm = bm * i

print(bj // bm)