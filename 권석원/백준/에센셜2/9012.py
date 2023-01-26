import sys
from collections import deque

N = int(sys.stdin.readline())

for i in range(N):
    line = deque(list(sys.stdin.readline().rstrip()))
    pos = 0
    while line:

        if pos+1 == len(line):
            print('NO')
            break

        if line[pos] == '(' and line[pos+1] == ')':
            del line[pos]
            del line[pos]
            
            if pos > 0:
                pos -= 1
        else:
            pos += 1

    if len(line) == 0:
        print('YES')
