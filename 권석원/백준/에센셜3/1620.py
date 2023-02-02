import sys

N, M = map(int,sys.stdin.readline().split())

poketmon_list = []

for _ in range(N):
    poketmon_list.append(sys.stdin.readline().rstrip())

for _ in range(M):
    q = sys.stdin.readline().rstrip()

    if q[0] <= '9' and q[0] >= '1':
        q = int(q)
        print(poketmon_list[q-1])
    else:
        print(poketmon_list.index(q)+1)
    