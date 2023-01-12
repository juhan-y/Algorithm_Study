import sys
input = sys.stdin.readline
arr = []
while True :
    temp = input().rstrip()
    if temp == '0' :
        break
    arr.append(temp)

for i in arr :
    flag = 0
    for j in range(len(i)//2) :
        if i[j] != i[-j-1] :
            print('no')
            flag = 1
            break
    if flag == 0 :
        print('yes')
    