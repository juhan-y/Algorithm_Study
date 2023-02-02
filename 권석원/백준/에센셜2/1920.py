import sys

N = int(sys.stdin.readline())
input_list = list(map(int,sys.stdin.readline().split()))
M = int(sys.stdin.readline())
check_list = list(map(int,sys.stdin.readline().split()))

tmp_set = set(input_list) & set(check_list)

for i in range(M):
    if check_list[i] in tmp_set:
        print(1)
    else:
        print(0)