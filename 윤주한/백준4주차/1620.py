import sys
n, m = map(int, input().split())
dic = dict()
dic2 = dict()
for i in range(1, n+1):
    mon = input()
    dic[str(i)] = mon
    dic2[mon] = str(i)

for _ in range(m):
    question = input()
    if ord(question[0]) >= 65:
        print(dic2[question])
    else:
        print(dic[question])