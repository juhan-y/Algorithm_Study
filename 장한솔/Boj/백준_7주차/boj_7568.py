import sys

N = int(sys.stdin.readline())
peo = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

for i in peo :
    cnt = 1
    for j in peo :
        if i[0] < j[0] and i[1] < j[1] :
            cnt += 1
    print(cnt, end = " ")