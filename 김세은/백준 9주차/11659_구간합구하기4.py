# 11659_구간 합 구하기 4
import sys

N, M = map(int, sys.stdin.readline().split())
S = list(map(int, sys.stdin.readline().split()))

cnt = 0
li=[0]
for i in S:
    cnt += i
    li.append(cnt)

for i in range(M):
    a, b = map(int, sys.stdin.readline().split())
    ans = li[b] - li[a-1]
    print(ans)
