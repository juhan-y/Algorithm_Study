import sys

M = int(sys.stdin.readline())
S = set()

for _ in range(M) :
    i = list(map(str, sys.stdin.readline().split()))
    if i[0] == "add" :
        S.add(int(i[1]))
    elif i[0] == "remove" :
        S.discard(int(i[1]))
    elif i[0] == "check" :
        if int(i[1]) in S :
            print(1)
        else :
            print(0)
    elif i[0] == "toggle" :
        if int(i[1]) in S :
            S.discard(int(i[1]))
        else :
            S.add(int(i[1]))
    elif i[0] == "all" :
        S = set([x for x in range(1, 21)])
    elif i[0] == "empty" :
        S = set()