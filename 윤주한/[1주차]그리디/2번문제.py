n, m, k = map(int, input().split())
ls = list(map(int, input().split()))

ls.sort(reverse=True)
cnt = 0
summation = 0
for _ in range(m):
    if cnt < 3:
        summation += ls[0]
        cnt += 1
    else:
        summation += ls[1]
        cnt = 0
print(summation)