import sys
input = sys.stdin.readline

arr=[]

while True:
    temp = list(map(int, input().split()))
    
    if max(temp) == 0 :
        break
    
    temp.sort()
    arr.append(temp)

for i in arr :
    if (i[0]**2)+(i[1]**2) == (i[2]**2) :
        print('right')
    else :
        print('wrong')
