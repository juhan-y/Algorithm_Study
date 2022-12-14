import sys

n = int(sys.stdin.readline())


def func(a,prev,next):
    if a == n:
        return prev
    
    return func(a+1,next,next+prev)
    

print(func(1,1,1))