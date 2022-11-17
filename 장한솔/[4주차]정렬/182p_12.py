import sys

N, K = map(int, sys.stdin.readline().split())

A = list(map(int, sys.stdin.readline().split()))
B = list(map(int, sys.stdin.readline().split()))

A.sort()
B.sort(reverse = True)

for i in range(K) :
    if A[i] >= B[i] :
        break
    else :
        A[i], B[i] = B[i], A[i]
        
print(sum(A))