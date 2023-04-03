import sys
from itertools import permutations

N, M = map(int, sys.stdin.readline().split())
num = list(map(int, sys.stdin.readline().split()))
num.sort()
arr = list(permutations(num, M))

for a in arr :
    print(*a)