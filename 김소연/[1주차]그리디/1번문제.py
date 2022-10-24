# 예제 1) 거스름돈
# 거스름돈 : 500,100,50,10
# 거슬러 줄 돈 : N (10의 배수)
# 거슬러 줄 최소 동전 수
# 큰 단위부터 !

import sys

def coins_prob(n):
    count = 0

    coins = [500, 100, 50, 10]
    for i in coins:
        count += (n // i)
        n %= i
        
    return count
    
print(coins_prob(1260))