n = int(input())

ls = []

for _ in range(n):
    x, y = map(int, input().split())
    ls.append((x, y))

ls1 = sorted(ls, key=lambda x : (-x[0], -x[1]))
ls2 = sorted(ls, key=lambda x : -x[1])

rank = 1
dic = dict()

dic[ls1[0]] = rank
prev = ls1[0]
cnt = 0
for i in range(1, n):
    if prev[0] > ls1[i][0]:
        if prev[1] > ls1[i][1]:
            rank += 1 + cnt
            cnt = 0
            prev = ls1[i]
        else:
            cnt += 1
    else:
        cnt += 1
    dic[ls1[i]] = rank

for i in ls:
    print(dic[i], end=' ')