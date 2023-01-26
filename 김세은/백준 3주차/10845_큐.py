# 10845 큐
import sys

N = int(input())

queue = []

for _ in range(N):
    li = sys.stdin.readline().split()

    if li[0] == 'push':
        queue.append(li[1])

    elif li[0] == 'pop':
        if len(queue)==0:
            print(-1)
        else:
            print(queue.pop(0))

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
