from itertools import combinations
import sys

N, M = map(int, sys.stdin.readline().split())
num = list(map(int, sys.stdin.readline().split()))
combi = list(combinations(num, 3))
result = 0

for i in combi :
    if sum(i) > M :
        continue
    else :
        result = max(result, sum(i))

print(result)