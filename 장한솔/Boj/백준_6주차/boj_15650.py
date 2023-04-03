import sys
from itertools import combinations

N, M = map(int, sys.stdin.readline().split())
arr = list(combinations([i for i in range(1, N+1)], M))

for a in arr :
    print(*a)