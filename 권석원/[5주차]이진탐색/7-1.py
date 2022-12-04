import sys

cnt, find = sys.stdin.readline().rstrip().split()

lst = list(sys.stdin.readline().rstrip().split())

for i in range(int(cnt)):
    if find == lst[i]:
        print(i+1)
        break