def fibonacci(x):
    if x == 1 or x == 2:
        return 1
    return fibonacci(x-1) + fibonacci(x-2)