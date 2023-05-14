import sys

N = int(sys.stdin.readline())
cnt = 0
start = 666

while True :
    if "666" in str(start) :
        cnt += 1

    start += 1

    if cnt == N :
        print(start-1)
        break