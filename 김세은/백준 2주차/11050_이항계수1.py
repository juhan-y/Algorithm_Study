# 11050 이항 계수1
N, K = map(int, input().split())

N1 = 1
for i in range(N-K+1, N+1, 1):
    N1 *= i
a = N1

K1 = 1
for j in range(K, 1, -1):
    K1 *= j
b = K1

ans = int(a/b)
print(ans)
