# 11650 좌표 정렬하기
import sys

N = int(input())

li = []
for i in range(N):
    x, y = map(int, sys.stdin.readline().split())
    li.append((x, y))

li.sort()

for i in li:
    print(i[0], i[1])
