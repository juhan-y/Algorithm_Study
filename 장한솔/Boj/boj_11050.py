import sys

N, K = map(int, sys.stdin.readline().split())

def fac(n) :
    if n == 0 :
        return 1
    return n * fac(n-1)

answer = fac(N) // (fac(K) * fac(N - K))

print(answer)