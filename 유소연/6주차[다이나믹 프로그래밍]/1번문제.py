def fibo(i):
    if i==1 or i==2:
        return 1
    return fibo(i-1)+fibo(i-2)

print(fibo(4))