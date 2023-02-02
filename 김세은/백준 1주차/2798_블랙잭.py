# 2798 블랙잭
from itertools import combinations

N, M = map(int, input().split())
li = list(map(int, input().split()))
li.sort(reverse=True)

com = list(combinations(li, 3))
ans = 0

for i in com:
    if (M >= sum(i)):
        ans = max(ans, sum(i))

print(ans)
