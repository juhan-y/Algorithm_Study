import sys

N = int(sys.stdin.readline())

input_list = list(map(int,sys.stdin.readline().split()))

list_sosu_bool = [True] * 1001
list_sosu_bool[0] = False
list_sosu_bool[1] = False


for i in range(2,1001):
    if list_sosu_bool[i]:
        for j in range(2,1000//i + 1):
            if i*j < 1001:
                list_sosu_bool[i*j] = False
            else:
                break

ans = 0

for i in input_list:
    if list_sosu_bool[i]:
        ans += 1

print(ans)
