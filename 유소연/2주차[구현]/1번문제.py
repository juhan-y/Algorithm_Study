import sys

count = sys.stdin.readline()
arr = list(sys.stdin.readline().split())
start = [1,1] 
dic = {'L':[0,-1], 'R':[0,1], 'U':[-1,0], 'D':[1,0]}

def travel(start, i) :
    temp0 = start[0] + dic[arr[i]][0]
    temp1 = start[1] + dic[arr[i]][1]

    if temp0 != 0 and temp1 != 0 :
        start[0] = temp0
        start[1] = temp1

    if i < 5 :
        travel(start, i+1)
    else :
        print(start)

travel(start, 0)