# 1620 나는야 포켓몬 마스터 이다솜
import sys

N, M = map(int, input().split())

d = {}
for i in range(1, N+1):
    name = sys.stdin.readline().strip()
    d[i] = name
    d[name] = i

for i in range(M):
    q = sys.stdin.readline().strip()
    if q.isdigit():
        print(d[int(q)])
    else:
        print(d[q])
