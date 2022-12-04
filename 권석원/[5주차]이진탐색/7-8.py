import sys

cnt, find = map(int,sys.stdin.readline().rstrip().split())
lst = list(map(int,sys.stdin.readline().split()))

start = 0
end = max(lst)

h = min(lst)


while end - start != 1:
    tmp = 0
    
    for l in lst:
        if l > h:
            tmp += l - h

    if tmp < find:
         end = h
    elif tmp > find:
        start = h
    else:
        print(h)
        break
        
    h = (end - start)//2 + start
    





