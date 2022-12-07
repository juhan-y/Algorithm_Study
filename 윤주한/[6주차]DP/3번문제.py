def fibonacci(x):
    print("f("+str(x)+")", end=' ')
    if x == 1 or x == 2:
        return 1
    return fibonacci(x-1) + fibonacci(x-2)


fibonacci(6)