import sys

N = int(sys.stdin.readline())

list_input = []

for _ in range(N):
    list_tmp = sys.stdin.readline().split()
    list_tmp[0] = int(list_tmp[0])
    list_input.append(list_tmp)

list_input.sort(key=lambda x : x[0])

for input in list_input:
    age, name = input[0], input[1]
    print(age,name)

