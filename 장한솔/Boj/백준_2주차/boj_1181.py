import sys

N = int(sys.stdin.readline())

wor = [sys.stdin.readline().strip() for _ in range(N)]
set_wor = set(wor)
wor = list(set_wor)

wor.sort(key = lambda x :(len(x), x))

for i in range(len(wor)) :
    print(wor[i])