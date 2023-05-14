a = input().strip()
b = input().strip()

a = " " + a
b = " " + b

len_a = len(a)
len_b = len(b)

d = [[0] * (len_b) for _ in range(len(a))]

for i in range(1, len_a):
    for j in range(1, len(b)):
        if a[i] == b[j]:
            d[i][j] = d[i-1][j - 1] + 1
        else:
            d[i][j] = max(d[i - 1][j], d[i][j - 1])

print(d[len_a - 1][len_b - 1])
