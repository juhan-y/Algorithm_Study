import sys

N, M = map(int, sys.stdin.readline().split())
A, B, d = map(int, sys.stdin.readline().split())
loc = [A,B]
dir = {0:[0,-1],1:[-1,0],2:[0,1],3:[1,0]}
b_dir = {0:[1,0],1:[0,-1],2:[-1,0],3:[0,1]}
flag = 1
arr = []
count = 0

for i in range(M) :
    temp = list(map(int, sys.stdin.readline().split()))
    arr.append(temp)

arr_clear = arr.copy()

def rot(d) :
    if d == 0 :
        d=3
    else :
        d-=1
    return d

def check(loc, d, flag) :
    #flag : 0 > 가보지 않은 칸 -1이하 > 가봤던칸
    temp0=loc[0]+dir[d][0]
    temp1=loc[1]+dir[d][1]

    if arr_clear[temp0][temp1]  == 0:
        arr_clear[temp0][temp1] = 1
        return([temp0, temp1],0)
    else :
        flag -=1
        return(loc,flag)

arr_clear[loc[0]][loc[1]] = 1

while True :
    d=rot(d)
    loc, flag = check(loc, d, flag)

    if flag == -4 :
        temp0=loc[0]+b_dir[d][0]
        temp1=loc[1]+b_dir[d][1]

        if arr[temp0][temp1] == 1 :
            break
        else :
            continue
    elif flag == 0 :
        count +=1
    else :
        continue


print(count)