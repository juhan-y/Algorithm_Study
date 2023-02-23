import sys

A = int(sys.stdin.readline())
A_num = list(map(int, sys.stdin.readline().split()))

graph = [1] * A

for i in range(1, A) :
    for j in range(i) :
        if A_num[i] > A_num[j] :
            graph[i] = max(graph[i], graph[j]+1)


print(max(graph))