import sys

N = int(sys.stdin.readline())
ti = list(map(int, sys.stdin.readline().split()))
ti.sort()

an = [0] * N
for i in range(N) :
    an[i] = sum(ti[:i+1])

print(sum(an))