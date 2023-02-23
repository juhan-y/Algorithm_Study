# 15829 Hashing
L = int(input())
s = input()

r = 31
M = 1234567891

ans = 0
for i in range(len(s)):
    a = ord(s[i]) - 96
    ans += a*(r**i)

print(ans%M)
