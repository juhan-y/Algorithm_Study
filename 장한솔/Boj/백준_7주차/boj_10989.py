import sys

N = int(sys.stdin.readline())
num = [0] * 10001

for _ in range(N) :
    i = int(sys.stdin.readline())
    num[i] += 1

for j in range(10001) :
    if num[j] != 0 :
        for _ in range(num[j]) :
            print(j)
