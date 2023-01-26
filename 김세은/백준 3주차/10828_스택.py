# 10828 스택
import sys

N = int(input())

stack = []

for _ in range(N):
    li = sys.stdin.readline().split()

    if li[0] == 'push':
        stack.append(li[1])
        
    elif li[0] == 'pop':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack.pop())
            
    elif li[0] == 'size':
        print(len(stack))
        
    elif li[0] == 'empty':
        if len(stack)==0:
            print(1)
        else:
            print(0)
            
    elif li[0] == 'top':
        if len(stack)==0:
            print(-1)
        else:
            print(stack[-1])
