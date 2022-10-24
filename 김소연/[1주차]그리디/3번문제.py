# 실전) 숫자카드 게임
# n*m 행렬의 카드에서 한 행을 고르고 그 행의 가장 작은 수 뽑기 -> 이때 뽑은 수가 가장 큰 수가 되도록
import sys

n,m = map(int, input().split())
cards = []

for _ in range(n):
    cards.append(list(map(int, input().split())))

for i in cards : 
    i.sort()
cards.sort()

answer = cards[-1][1]
print(answer)


# # 실전) 숫자카드 게임
# # list 간의 value 비교 python은 가능 
# n,m = map(int, input().split())
# cards = []
# m = []

# # list 간의 value 비교 python은 가능 
# for i in range(n):
#     cards.append(list(map(int, input().split())))
#     min_val = min(cards[i])
#     m.append(min_val)

# answer = max(m)

# print(answer)