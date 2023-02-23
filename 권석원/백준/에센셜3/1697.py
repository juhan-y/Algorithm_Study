import sys
from collections import deque

N, K = map(int,sys.stdin.readline().split())

hns_list = [1000001] * 1000001
hns_list[N] = 0

q = deque()
q.append(N)

while q:
    i = q.popleft()

    if i == K:
        if hns_list[i]:
            print(hns_list[i])
        else:
            print(0)
        break


    if i+1 < 1000001:
        hns_list[i+1] = min(hns_list[i]+1,hns_list[i+1])
        if hns_list[i+1] == hns_list[i]+1:
            q.append(i+1)
    
    if i*2 < 1000001:
        hns_list[i*2] = min(hns_list[i]+1,hns_list[i*2])
        if hns_list[i*2] == hns_list[i]+1:
            q.append(i*2)

    if 0 <= i-1:
        hns_list[i-1] = min(hns_list[i]+1,hns_list[i-1])
        if hns_list[i-1] == hns_list[i]+1:
            q.append(i-1)
    


