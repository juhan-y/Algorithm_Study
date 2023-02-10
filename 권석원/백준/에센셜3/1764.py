import sys

N, M = map(int,sys.stdin.readline().split())

d_list = []
b_list = []

for _ in range(N):
    d_list.append(sys.stdin.readline().rstrip())

for _ in range(M):
    b_list.append(sys.stdin.readline().rstrip())

ans = list(set(d_list) & set(b_list))

print(len(ans))
ans.sort()
for a in ans:
    print(a)