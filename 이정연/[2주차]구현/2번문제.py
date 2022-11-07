#!/usr/bin/env python
# coding: utf-8

# In[1]:


n = int(input())

count = 0
# N시까지를 범위로
for i in range(n + 1):
    # 분
    for j in range(60):
        # 초
        for k in range(60):
            if '3' in str(i) + str(j) + str(k):
                count += 1
                
print(count)


# In[ ]:




