# 팩토리럴 
import sys 

# 반복 n!
def factorial(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result

# 재귀 n!
def factorial_re(n):
    if n<= 1:
        return 1
    return n * factorial_re(n-1)

print(factorial(5))
print(factorial_re(5))