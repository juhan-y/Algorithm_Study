## LCS (최장 공통 부분 수열)
import sys
input = sys.stdin.readline
a = input().strip()
b = input().strip()
a, b = " " + a, " " + b

graph = [[0] * len(b) for _ in range(len(a))]

for i in range(1,len(a)):
    for j in range(1,len(b)):
        if a[i] == b[j]:
            graph[i][j] = graph[i-1][j-1] + 1
        else:
            graph[i][j] = max(graph[i][j-1], graph[i-1][j])
print(graph)
print(graph[len(a)-1][len(b)-1])