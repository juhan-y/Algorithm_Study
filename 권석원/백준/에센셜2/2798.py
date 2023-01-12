import sys
from itertools import combinations

n,m = map(int,sys.stdin.readline().split())

cards = list(map(int,sys.stdin.readline().split()))

comb = list(combinations(cards,3))

sum_comb = []

for c in comb:
    sum_comb.append(sum(c))

max_val = 0

for sum in sum_comb:
    max_tmp = max(sum,max_val)
    
    if max_tmp <= m:
         max_val = max_tmp
         
print(max_val)