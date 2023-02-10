import sys

N = int(sys.stdin.readline())

num_list = list(map(int,sys.stdin.readline().split()))
num_list.sort()


sum_tmp = 0
ans_list = []

for num in num_list:
    sum_tmp += num
    ans_list.append(sum_tmp)

print(sum(ans_list))
