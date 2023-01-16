# 2751 수 정렬하기2
import sys

N = int(input())

li = []
for i in range(N):
    li.append(int(sys.stdin.readline()))
    
li.sort()

for i in li:
    sys.stdout.write(str(i)+'\n')
