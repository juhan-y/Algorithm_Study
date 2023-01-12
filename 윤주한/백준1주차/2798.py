from itertools import combinations
n, m = map(int, input().split())

ls = list(map(int, input().split()))

max_sum = 0
for a, b, c in combinations(ls, 3):
  if a + b + c <= m:
    max_sum = max(max_sum, a + b + c)

print(max_sum)