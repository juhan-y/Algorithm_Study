from itertools import combinations
n, m = map(int, input().split())
ls = list(range(1, n+1))

for i in combinations(ls, m):
    for j in i:
        print(j, end=' ')
    print()