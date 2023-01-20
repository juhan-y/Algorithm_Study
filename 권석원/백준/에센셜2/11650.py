import sys

N = int(sys.stdin.readline())

list_sort = []

for _ in range(N):
    input_tmp = list(map(int,sys.stdin.readline().split()))
    list_sort.append(input_tmp)

list_sort.sort()

for sorted in list_sort:
    print(sorted[0],sorted[1])