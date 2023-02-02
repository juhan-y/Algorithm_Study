import sys

N, M = map(int, sys.stdin.readline().split())
poketmon = {}

for i in range(N) :
    po = sys.stdin.readline().strip()
    poketmon[i + 1] = po
    poketmon[po] = i + 1

for j in range(M) :
    pro = sys.stdin.readline().strip()
    if pro.isdigit() :
        print(poketmon[int(pro)])
    else :
        print(poketmon[pro])