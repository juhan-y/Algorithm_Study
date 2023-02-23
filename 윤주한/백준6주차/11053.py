n = int(input())

ls = list(map(int, input().split()))

d = [1] * n

for i in range(1, n):
    for j in range(i, -1, -1):
        if ls[j] < ls[i]:
            d[i] = max(d[i], d[j] + 1)

print(max(d))