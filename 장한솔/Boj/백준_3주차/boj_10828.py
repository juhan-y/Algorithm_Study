import sys

N = int(sys.stdin.readline())
nstack = [list(map(str, sys.stdin.readline().split())) for _ in range(N)]
answer = []

for i in nstack :
    if i[0] == "push" :
        answer.append(i[1])
    elif i[0] == "pop" :
        if len(answer) != 0 :
            print(answer.pop())
        else :
            print(-1)
    elif i[0] == "size" :
        print(len(answer))
    elif i[0] == "empty" :
        if len(answer) == 0 :
            print(1)
        else :
            print(0)
    elif i[0] == "top" :
        if len(answer) != 0:
            print(answer[-1])
        else:
            print(-1)