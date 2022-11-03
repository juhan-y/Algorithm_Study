#!/usr/bin/env python
# coding: utf-8

# In[1]:


n = input()

# 나이트의 움직임
moves = [(-2, -1), (-2, 1), (-1, -2), (-1, 2),
          (2, 1), (2, -1), (1, -2), (1, 2)]

# 숫자
row = int(n[1])

# 알파벳 -> 숫자
column = n[0]
col_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8}
column = col_dict[column]

result = 0
for move in moves:
    # 모든 경우를 순차적으로 검증
    next_row = row + move[0]
    next_column = column + move[1]
    
    # 범위 내에 있을 경우만 + 1
    if next_row >= 1 and next_row <= 8 and next_column >= 1 and next_column <= 8:
        result += 1
        
print(result)


# In[ ]:




