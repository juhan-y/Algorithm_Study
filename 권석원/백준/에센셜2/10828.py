import sys
N = int(sys.stdin.readline())

stack = []

for _ in range(N):
    line = list(sys.stdin.readline().rstrip().split())
    if len(line) == 2:
        stack.append(int(line[1]))
    else:
        if line[0] == 'top':
            if stack:
                print(stack[len(stack)-1])
            else:
                print(-1)
        elif line[0] == 'size':
            print(len(stack))
        elif line[0] == 'empty':
            if stack:
                print(0)
            else:
                print(1)
        elif line[0] == 'pop':
            if stack:
                stack.pop()
            else:
                print(-1)
