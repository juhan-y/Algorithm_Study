import sys

N, M = map(int,sys.stdin.readline().split())

map_list = []

for i in range(N):
    map_list.append(list(sys.stdin.readline().rstrip()))

for i in range(N):
    for j in range(M):
        if j + 7 >= len(map_list[0]) or i + 7 >= len(map_list): # 8*8일 수 없으면 통과
            continue

        


