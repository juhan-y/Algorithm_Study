# 18870 좌표 압축
import sys

N = int(sys.stdin.readline())
li = list(map(int, sys.stdin.readline().split()))

li2 = list(set(li))
li2.sort()

d = {}
for i in range(len(li2)):
    d[li2[i]] = i

for i in li:
      print(d[i], end=' ')
