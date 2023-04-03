import sys
input = sys.stdin.readline
n = int(input())
q = []
dic = dict()
for _ in range(n):
    a = int(input())
    if a not in dic.keys():
        dic[a] = 0
    dic[a] += 1

ls = list(dic.items())
ls.sort()
for i in ls:
    for _ in range(i[1]):
        print(i[0])