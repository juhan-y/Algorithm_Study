#!/usr/bin/env python
# coding: utf-8

# In[3]:


n = int(input())
directions = input().split()


# In[6]:


move = ['L', 'R', 'U', 'D']
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
x, y = 1, 1


# In[7]:


for i in range(len(directions)):
    for j in range(len(move)):
        if directions[i] == move[j]:
            tmp_x = x + dx[j]
            tmp_y = y + dy[j]
            
    if tmp_x < 1 or tmp_x > n or tmp_y < 1 or tmp_y > n:
        continue
        
    x, y = tmp_x, tmp_y
    
print(x, y)


# In[ ]:




