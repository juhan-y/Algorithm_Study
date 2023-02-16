# 1764 듣보잡
import sys

N, M = map(int, sys.stdin.readline().split())

li1 = []
li2 = []
for i in range(N):
    a = sys.stdin.readline().strip()
    li1.append(a)

for j in range(M):
    b = sys.stdin.readline().strip()
    li2.append(b)

li1 = set(li1)
li2 = set(li2)

ans = []
for i in li1:
    if i in li2:
        ans.append(i)
ans.sort()

print(len(ans))
for i in ans:
    print(i)
