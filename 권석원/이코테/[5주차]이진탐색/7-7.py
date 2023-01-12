import sys

cnt = int(sys.stdin.readline())
lst = list(map(int,sys.stdin.readline().split()))

find_cnt = int(sys.stdin.readline())
find_lst = list(map(int,sys.stdin.readline().split()))

for find in find_lst:
    if find in lst:
        print('yes',end='')
    else:
        print('no',end='')