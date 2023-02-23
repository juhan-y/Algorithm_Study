# 10989 수 정렬하기 3
import sys

N = int(sys.stdin.readline())

li = [0]*10001
for i in range(N):
    a = int(sys.stdin.readline())
    li[a] += 1

for i in range(len(li)):
    if li[i] != 0:
        for j in range(li[i]):
            print(i)
