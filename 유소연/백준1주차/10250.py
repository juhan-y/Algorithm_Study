import sys
input = sys.stdin.readline

t = int(input())
arr = []

for i in range(t) :
    temp = list(map(int, input().split()))
    arr.append(temp)

for h,w,n in arr :
    if n%h == 0 :
        answer = h*100+(n//h)
    else : 
        answer = (n%h)*100+(n//h+1)
    print(answer)