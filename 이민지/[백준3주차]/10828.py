# readline, readline, readline!!

import sys

n = int(sys.stdin.readline())
stack = []

for _ in range(n):
    cmd = sys.stdin.readline().split()
    if cmd[0] == "push":
        stack.append(cmd[1])
    if cmd[0] == "pop":
        if len(stack)!=0:
            print(stack.pop())
        else:
            print(-1)
    if cmd[0] == "size":
        print(len(stack))
    if cmd[0] == "empty":
        if len(stack)!=0:
            print(0)
        else:
            print(1)
    if cmd[0] == "top":
        if len(stack)!=0:
            print(stack[-1])
        else:
            print(-1)