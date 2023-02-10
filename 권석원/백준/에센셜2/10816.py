import sys
from collections import Counter

N = int(sys.stdin.readline())
input_list = list(map(int,sys.stdin.readline().split()))
M = int(sys.stdin.readline())
check_list = list(map(int,sys.stdin.readline().split()))

input_counter = Counter(input_list)
ans_list = []

for check in check_list:
    if check in input_counter:
        print(input_counter[check],end=' ')
    else:
        print(0,end=' ')

