import sys

N = int(sys.stdin.readline())
num = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

num.sort(key = lambda x : (x[0], x[1]))

for i in range(N) :
    print(num[i][0], num[i][1], sep = ' ')