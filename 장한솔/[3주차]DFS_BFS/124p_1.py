stack = []

stack.append(5) # 5삽입 5
stack.append(2) # 2삽입 5 2
stack.append(3) # 3삽입 5 2 3
stack.append(7) # 7삽입 5 2 3 7
stack.pop() # 7삭제 (제일 늦게 들어온 원소 제거) 5 2 3
stack.append(1) # 1삽입 5 2 3 1
stack.append(4) # 4삽입 5 2 3 1 4
stack.pop() # 4삭제 (제일 늦게 들어온 원소 제거) 5 2 3 1

print(stack) # 5 2 3 1 출력
print(stack[::-1]) # 1 3 2 5 출력