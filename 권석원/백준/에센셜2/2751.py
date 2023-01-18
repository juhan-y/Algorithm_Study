import sys

N = int(sys.stdin.readline())
list_input = []

for _ in range(N):
    list_input.append(int(sys.stdin.readline()))

list_input.sort()

for input in list_input:
    print(input)
