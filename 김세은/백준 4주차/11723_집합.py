# 11723 집합
import sys

M = int(input())

S = set()
for _ in range(M):
    li = sys.stdin.readline().split()

    if len(li)==1:
        if li[0] == 'all':
            S = set([i for i in range(1, 21)])
        else:
            S = set()

    else:
        x = int(li[1])

        if li[0] == 'add':
            S.add(x)

        elif li[0] == 'remove':
            if x in S:
                S.discard(x)
            else:
                continue

        elif li[0] == 'check':
            if x in S:
                print(1)
            else:
                print(0)

        elif li[0] == 'toggle':
            if x in S:
                S.discard(x)
            else:
                S.add(x)
