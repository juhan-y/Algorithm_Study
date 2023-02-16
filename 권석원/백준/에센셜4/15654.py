import sys

n,m = map(int,sys.stdin.readline().split())
num_list = list(map(int,sys.stdin.readline().split()))
num_list.sort()
check_list = [False] * n

print_list = []

def func(cnt,check):
    global print_list

    if cnt == m:
        for i in print_list:
            print(i, end=' ')
        print()
        return
    
    for k in range(0,n):

        if cnt == 0:
            print_list.clear()

        if check[k] == False:
            check[k] = True
            print_list.append(num_list[k])
            func(cnt+1,check)
            print_list.pop()
            check[k] = False

func(0,check_list)
