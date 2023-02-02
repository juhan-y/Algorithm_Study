# 10866 덱
import sys
from collections import deque

N = int(input())

queue = deque()

for _ in range(N):
    li = sys.stdin.readline().split()

    if li[0] == 'push_front':
        queue.appendleft(li[1])

    elif li[0] == 'push_back':
        queue.append(li[1])

    elif li[0] == 'pop_front':
        if len(queue)==0:
            print(-1)
        else:
            print(queue[0])
            queue.popleft()

    elif li[0] == 'pop_back':
        if len(queue)==0:
            print(-1)
        else:
            print(queue[-1])
            queue.pop()

    elif li[0] == 'size':
        print(len(queue))

    elif li[0] == 'empty':
        if len(queue)==0:
            print(1)
        else:
            print(0)

    elif li[0] == 'front':
        if len(queue)==0:
            print(-1)
        else:
            print(queue[0])

    elif li[0] == 'back':
        if len(queue)==0:
            print(-1)
        else:
            print(queue[-1])
