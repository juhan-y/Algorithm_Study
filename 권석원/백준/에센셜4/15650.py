import sys

n,m = map(int,sys.stdin.readline().split())

check_list = [False] * (n+1)

def func(num,cnt,check):
    if cnt == m:
        for i in range(len(check)):
            if check[i]:
                print(i, end=' ')
        print()
        return
    
    for k in range(num,n+1):
        if check[k] == False:
            check[k] = True
            func(k+1,cnt+1,check)
            check[k] = False

func(1,0,check_list)
