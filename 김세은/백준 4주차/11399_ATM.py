# 11399 ATM
N = int(input())
P = list(map(int, input().split()))

P.sort()

cnt = 0
ans = 0
for i in P:
    cnt += i
    ans += cnt

print(ans)
