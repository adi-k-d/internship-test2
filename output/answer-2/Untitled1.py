#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# In[2]:


df=pd.read_csv('main.csv')
df


# In[4]:


print(df.groupby('occupation').agg({'age':['min','max']}))


# In[ ]:




