import sys

start = sys.stdin.readline()

dic = {'a':1, 'b':2, 'c':3, 'd':4, 'e':5, 'f':6, 'g':7, 'h':8}
start = [dic[start[0]],int(start[1])]

arr = [[-2,1],[-2,-1],[2,1],[2,-1],[-1,2],[-1,-2],[1,2],[1,-2]]

count = 0

for i in arr :
    temp = start[0]+i[0]
    temp1 = start[1]+i[1]

    if temp >0 and temp1 >0 :
        count +=1

print(count)
