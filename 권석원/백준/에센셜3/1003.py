import sys
    
T = int(sys.stdin.readline())

for _ in range(T):

    N = int(sys.stdin.readline())

    if N == 0:
        print(1,0)
        continue
    elif N == 1:
        print(0,1)
        continue

    fibo = [0,1]

    for i in range(N):
        fibo.append(fibo[i] + fibo[i+1])

    print(fibo[N-1],fibo[N])

