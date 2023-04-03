L = int(input())
char = input()
ls = []
for i in char:
    ls.append(i)

ans = 0
for i in range(L):
    ans += (ord(ls[i]) - ord('a') + 1) * (31 ** i)

print(ans % 1234567891)