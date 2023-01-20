import sys

N = int(sys.stdin.readline())
num = list(map(int, sys.stdin.readline().split()))
pri = 0

for i in num :
    cnt = 0
    if i > 1 :
        for j in range(2, i) :
            if i % j == 0 :
                cnt += 1
        if cnt == 0 :
            pri += 1

print(pri)