import sys

N,K = map(int,sys.stdin.readline().split())

denominator_1 = 1
denominator_2 = 1
numerator = 1

# for i in range(2,N+1):
#     numerator *= i

# for i in range(2,K+1):
#     denominator_1 *= i

# for i in range(2,(N-K)+1):
#     denominator_2 *= i

# print(numerator//(denominator_1 * denominator_2))

n = N

while n > 1:
    numerator *= n

    if n <= N - K :
        denominator_1 *= n
    if n <= K:
        denominator_2 *= n

    n -= 1

print(numerator//(denominator_1 * denominator_2))
