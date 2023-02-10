import sys
from collections import deque

input=sys.stdin.readline
q = deque()
n = int(input())
for _ in range(n):
    order = input().lstrip().rstrip()
    if len(order) == 3:
        if order == 'pop':
            if len(q) == 0:
                print(-1)
            else:
                print(q.popleft())
        elif order == 'top':
            if len(q) == 0:
                print(-1)
            else:
                print(q[-1])
    else:
        if order[:4] == 'push':
            order, num = order.split()
            q.append(num)
        elif order == 'size':
            print(len(q))
        elif order == 'empty':
            if len(q) == 0:
                print(1)
            else:
                print(0)
        elif order == 'front':
            if len(q) == 0:
                print(-1)
            else:
                print(q[0])
        elif order == 'back':
            if len(q) == 0:
                print(-1)
            else:
                print(q[-1])