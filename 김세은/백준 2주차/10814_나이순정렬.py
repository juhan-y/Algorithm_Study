# 10814 나이순 정렬
import sys

N = int(input())

li = []
for i in range(N):
    a, b = map(str, sys.stdin.readline().split())
    a = int(a)
    li.append((a, b))

li.sort(key = lambda x : x[0])

for i in li:
    print(i[0], i[1])
