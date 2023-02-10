## DP -> 질문게시판의 반례나 테케 모두 맞는데도 불구하고 통과못함 ㅠㅠ
# import sys
# input = sys.stdin.readline
# n = int(input())
# dic = dict()

# for _ in range(n):
#     a, b = map(int, input().split())
#     if b not in dic.keys():
#         dic[b] = [a]
#     else:
#         dic[b].append(a)
# d = [0] * (100001)

# for i in dic.keys():
#     dic[i].sort()

# for i in range(100001):
#     d[i] = max(d[i], d[i-1])
#     if i in dic.keys():
#         for j in dic[i]:
#             d[i] = max(d[j] + 1, d[i-1])

# print(max(d))

import sys
input = sys.stdin.readline
n = int(input())

ls = []
for _ in range(n):
    a, b = map(int, input().split())
    ls.append((a, b))

ls.sort(key = lambda x: (x[1], x[0]))

cnt = 1
next = ls[0][1]
for i in ls[1:]:
    if next <= i[0]:
        cnt += 1
        next = i[1]

print(cnt)