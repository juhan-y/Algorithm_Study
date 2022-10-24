import sys

num = int(sys.stdin.readline())

won = 0
lst = [500, 100, 50, 10]
for i in lst:
    sum = num // i
    won += sum
    num -= (i * sum)

print(won)