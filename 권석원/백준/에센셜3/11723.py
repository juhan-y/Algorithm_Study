import sys

N = int(sys.stdin.readline())

S = [0 for _ in range(21)]

for _ in range(N):
    input_list = list(map(str,sys.stdin.readline().split()))

    cmd = input_list[0]

    if len(input_list) > 1:
        num = int(input_list[1])

    if cmd == 'add':
        if S[num] == 0:
            S[num] = 1
    elif cmd == 'remove':
        if S[num] == 1:
            S[num] = 0
    elif cmd == 'check':
        if S[num] == 1:
            print(1)
        else:
            print(0)
    elif cmd == 'toggle':
        if S[num] == 1:
            S[num] = 0
        else:
            S[num] = 1
    elif cmd == 'all':
        S = [1 for _ in range(21)]
    elif cmd == 'empty':
        S = [0 for _ in range(21)]