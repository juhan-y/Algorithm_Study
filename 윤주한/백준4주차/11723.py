import sys
s = set()
n = int(sys.stdin.readline())

for _ in range(n):
    order = sys.stdin.readline().split()
    if order[0] == 'add':
        if int(order[1]) not in s:
            s.add(int(order[1]))
    elif order[0] == 'remove':
        if int(order[1]) in s:
            s.remove(int(order[1]))
    elif order[0] == 'check':
        if int(order[1]) in s:
            print(1)
        else:
            print(0)
    elif order[0] == 'toggle':
        if int(order[1]) in s:
            s.remove(int(order[1]))
        else:
            s.add(int(order[1]))
    elif order[0] == 'all':
        s = set(range(1,21))
    elif order[0] == 'empty':
        s = set()

