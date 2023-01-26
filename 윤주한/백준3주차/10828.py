import sys

input=sys.stdin.readline
stack = []
n = int(input())
for _ in range(n):
    order = input().lstrip().rstrip()
    if len(order) == 3:
        if order == 'pop':
            if len(stack) == 0:
                print(-1)
            else:
                print(stack.pop())
        elif order == 'top':
            if len(stack) == 0:
                print(-1)
            else:
                print(stack[-1])
    else:
        if order[:4] == 'push':
            order, num = order.split()
            stack.append(num)
        elif order == 'size':
            print(len(stack))
        elif order == 'empty':
            if len(stack) == 0:
                print(1)
            else:
                print(0)