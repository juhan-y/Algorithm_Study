import sys

T = int(sys.stdin.readline())

for i in range(T) :
    K = int(sys.stdin.readline())
    N = int(sys.stdin.readline())
    peo0 = [i for i in range(1, N+1)] # 0층사람

    for j in range(K) :
        hou = []
        for m in range(N) :
            hou.append(sum(peo0[:m+1]))
        peo0 = hou.copy() # 1층, 2층.. 계속 리뉴얼

    print(peo0[-1])