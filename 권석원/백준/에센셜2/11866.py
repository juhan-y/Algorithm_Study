import sys

N, K = map(int,sys.stdin.readline().split())

pos_list = [i for i in range(N+1)]
pos = 0

print('<',end='')

ans_list = []

while True:
    n = len(pos_list) -1
    pos += K

    if max(pos_list) == 0:
        break
    
    while pos > n:
        pos -= n

    ans_list.append(pos_list[pos])

    del pos_list[pos]
    pos -= 1

for ans in ans_list[:-1]:
    print(ans,end=', ')


print(str(ans_list[len(ans_list)-1]) + '>')