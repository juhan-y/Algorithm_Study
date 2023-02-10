# 9012 괄호
N = int(input())

for i in range(N):
    stack = []
    T = input()
    for j in T:
        if j=='(':
            stack.append(j)
        if j==')':
            if stack:
                stack.pop()
            else:
                stack.append(j)
            
    if len(stack) == 0:
        print('YES')
    else:
        print('NO')
