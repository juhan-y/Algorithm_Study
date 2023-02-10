import sys
from collections import deque

N = int(sys.stdin.readline())
ndq = [list(map(str, sys.stdin.readline().split())) for _ in range(N)]

dq = deque()

for i in ndq :
    if i[0] == "push_front" :
        dq.appendleft(i[1])
    elif i[0] == "push_back" :
        dq.append(i[1])
    elif i[0] == "pop_front" :
        if len(dq) != 0 :
            print(dq.popleft())
        else :
            print(-1)
    elif i[0] == "pop_back" :
        if len(dq) != 0 :
            print(dq.pop())
        else :
            print(-1)
    elif i[0] == "size" :
        print(len(dq))
    elif i[0] == "empty" :
        if len(dq) == 0 :
            print(1)
        else :
            print(0)
    elif i[0] == "front" :
        if len(dq) == 0 :
            print(-1)
        else :
            print(dq[0])
    elif i[0] == "back" :
        if len(dq) == 0 :
            print(-1)
        else :
            print(dq[-1])