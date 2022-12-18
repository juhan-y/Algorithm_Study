import sys

N = int(sys.stdin.readline())

num = [int(sys.stdin.readline()) for i in range(N)]

num.sort(reverse = True)

for i in num :
    print(i, end = ' ')