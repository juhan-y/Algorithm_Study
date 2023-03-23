# 1912_연속합
n = int(input())
s = list(map(int, input().split()))

for i in range(1, n):
    s[i] = max(s[i], s[i-1]+s[i])

ans = max(s)
print(ans)
