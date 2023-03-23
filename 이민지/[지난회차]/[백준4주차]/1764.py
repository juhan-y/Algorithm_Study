# 집합 사용
import sys
n, m = map(int, sys.stdin.readline().split())
a = set()
b = set()
for _ in range(n):
    a.add(sys.stdin.readline().strip())
for _ in range(m):
    b.add(sys.stdin.readline().strip())
ans = sorted(list(a&b))
print(len(ans))
for i in ans:
    print(i)