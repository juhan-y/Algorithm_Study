import sys

N = int(sys.stdin.readline())
peo = []

for _ in range(N) :
    a, b = map(str, sys.stdin.readline().split())
    peo.append([int(a), b])

peo.sort(key=lambda x : (x[0]))

for i in range(N) :
    print(peo[i][0], peo[i][1], sep = " ")