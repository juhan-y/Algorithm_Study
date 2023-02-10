# set(집합) 사용
# x를 int형으로 변환해야한다

import sys
m = int(sys.stdin.readline())
S = set()
for _ in range(m):
    words = sys.stdin.readline().split()
    if len(words) == 1:
        if words[0] == 'all':
            S = set(range(1,21))
        if words[0] == 'empty':
            S = set()
    else:
        x = int(words[1])
        if words[0] == 'add':
            S.add(x)
        if words[0] == 'remove':
            S.discard(x)
        if words[0] == 'check':
            if x in S:
                print(1)
            else:
                print(0)
        if words[0] == 'toggle':
            if x in S:
                S.discard(x)
            else:
                S.add(x)

