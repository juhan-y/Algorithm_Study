import sys
from collections import deque

input=sys.stdin.readline
q = deque()
n = int(input())
for _ in range(n):
    order = input().lstrip().rstrip()
    if len(order) > 5:
        if order[:4] == 'push':
            order, num = order.split()
            if order == 'push_front':
                q.appendleft(num)
            else:
                q.append(num)
        else:
            if len(q) == 0:
                print(-1)
            else:
                if order == 'pop_front':
                    print(q.popleft())
                else:
                    print(q.pop())
    else:
        if order == 'size':
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