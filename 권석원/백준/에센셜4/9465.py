import sys

T = int(sys.stdin.readline())

for _ in range(T):
    N = int(sys.stdin.readline())

    sticker_list = []
    d = []

    for _ in range(2):
        sticker_list.append(list(map(int,sys.stdin.readline().split())))
        d.append([0]*N)
    
    d[0][0] = sticker_list[0][0]
    d[1][0] = sticker_list[1][0]

    for i in range(1,N):
        d[0][i] = max(d[0][i], d[1][i-1] + sticker_list[0][i])
        d[1][i] = max(d[1][i], d[0][i-1] + sticker_list[1][i])

        if i-2 >= 0:
            d[0][i] = max(d[0][i], d[1][i-2] + sticker_list[0][i], d[0][i-2] + sticker_list[0][i])
            d[1][i] = max(d[1][i], d[0][i-2] + sticker_list[1][i], d[1][i-2] + sticker_list[1][i])
    
    print(max(d[0][N-1],d[1][N-1]))
    
    