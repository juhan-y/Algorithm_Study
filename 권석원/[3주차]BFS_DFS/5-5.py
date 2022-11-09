def func(i,m,n):
    if n < i:
        return m
    
    return func(i+1,m*i,n)

def func2(n):
    res = 1
    for i in range(1,n+1):
        res *= i
    
    return res
        

print(func(1,1,5))
print(func2(5))