#!/usr/bin/env python
# coding: utf-8

# # BubbleSort Algorithm

# In[2]:


import random as rnd
import numpy as np


# In[45]:


def create_list(x):
    list_1 = []
    for i in range(x):
        e = rnd.randint(-30,30)
        list_1.append(e)
    return list_1


# In[49]:


list_1 = create_list(10)
list_1


# In[50]:


for i in range(len(list_1)):
    if i+1 < len(list_1): #if "i" is bigger than "len(list)" loop is over
        for j in range(len(list_1) - i - 1 ): #compare item within other items
            if list_1[j+1] < list_1[j]:
                second = list_1[j]
                list_1[j] = list_1[j+1]
                list_1[j+1] = second
                
                


# In[51]:


list_1


# In[ ]:




