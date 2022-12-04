import sys

cnt, find = map(int,sys.stdin.readline().rstrip().split())

lst = list(map(int,sys.stdin.readline().rstrip().split()))

lst.sort()

n_to,n_from = 0,len(lst)-1
ans = False
while n_from - n_to != 1:

    mid = (n_from - n_to)//2 + n_to
    
    if lst[mid] > find:
        n_from = mid
        if lst[n_to] == find:
            print(n_to +1)
            ans = True
            break
    elif lst[mid] < find:
        n_to = mid
        if lst[n_from] == find:
            print(n_from +1)
            ans = True
            break
    else:
        print(mid+1)
        ans = True
        break
    

if ans == False:
    print('원소가 존재하지 않습니다.')
