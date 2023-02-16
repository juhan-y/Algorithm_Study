T = int(input())

for _ in range(T):
    stack = []
    isVPS = True
    arr = input()
    for i in arr:
        stack.append(i)
        if i == ')':
            stack.pop()
            if len(stack) == 0:
                isVPS = False            
            else:
                stack.pop()
    if len(stack) != 0:
        isVPS = False
    if isVPS:
        print("YES")
    else:
        print("NO")

