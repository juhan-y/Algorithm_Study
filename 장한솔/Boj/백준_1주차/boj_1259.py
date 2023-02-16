import sys

while(True) :
    S = sys.stdin.readline().strip()
    if S == '0' :
        break

    if S == S[::-1] :
        print('yes')
    else :
        print('no')