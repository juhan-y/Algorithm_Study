import sys

N, M, K = map(int, sys.stdin.readline().split())
num = list(map(int, sys.stdin.readline().split()))

num.sort()

a = num[-1] * K + num[-2]

ans = a * (M / (K+1)) + num[-1] * (M % (K+1))

print(int(ans))
