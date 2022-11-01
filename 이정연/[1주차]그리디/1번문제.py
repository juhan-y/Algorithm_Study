#!/usr/bin/env python
# coding: utf-8

# In[9]:


n = 1260
count = 0
coins = [500, 100, 50, 10]

for coin in coins:
    count += n // coin
    n = n % coin
    
print(count)


# In[ ]:




