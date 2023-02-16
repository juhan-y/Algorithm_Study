import sys

N = int(sys.stdin.readline())
input_list = list(map(int,sys.stdin.readline().split()))

d = [1] * (N+1)

for i in range(len(input_list)):
    for j in range(i):
        if input_list[i] <= input_list[j]:
            continue

        d[i] = max(d[j]+1,d[i])


print(max(d))





