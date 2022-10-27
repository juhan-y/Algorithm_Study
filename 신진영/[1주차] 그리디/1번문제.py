num = 1260
coin = [500, 100, 50, 10]
cnt = 0

for c in coin:
    cnt += num // c
    num = num - (c * (num // c))
print(cnt)