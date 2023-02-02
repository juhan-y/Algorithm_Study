import sys
from collections import deque

N = int(sys.stdin.readline())

tmp_list = deque([i for i in range(1,N+1)])

while len(tmp_list) > 1:
    tmp_list.popleft()

    tmp_list.append(tmp_list[0])
    tmp_list.popleft()

print(tmp_list[0])