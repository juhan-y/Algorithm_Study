import sys

N,M = map(int,sys.stdin.readline().rstrip().split())

card_lst = []

for i in range(N):
    lst = list(map(int,sys.stdin.readline().rstrip().split()))
    num = min(lst)
    card_lst.append(num)
    
print(max(card_lst))
    

          