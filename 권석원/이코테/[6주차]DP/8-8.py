import sys

a,b = map(int,sys.stdin.readline().split())
lst = []

for i in range(a):
    lst.append(int(sys.stdin.readline()))

cnt_lst = []

def func(x,cnt):
    if x < 0:
        return -1
    elif x == 0:
        return cnt
    
    for l in lst:
        tmp = func(x-l,cnt+1)
        if tmp is not None:
            cnt_lst.append(tmp)
        
func(b,0)      

p_list = []

for c in cnt_lst:
    if c > 0:
        p_list.append(c)

if len(p_list) > 0 :
    print(min(p_list))
else:
    print(-1)
    