import sys

T = int(sys.stdin.readline())

for _ in range(T) :
    H, W, N = map(int, sys.stdin.readline().split())
    ch = N % H
    room = (N // H) + 1

    if ch == 0 :
        ch = H
        room -= 1

    print(ch*100 + room)