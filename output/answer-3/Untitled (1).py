#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# In[2]:


df1=pd.read_csv('main.csv')


# In[3]:


df2=(df1.sort_values(by=['Red Cards','Yellow Cards'],ascending=False))


# In[4]:


b=df2[['Team','Red Cards','Yellow Cards']]
b


# In[5]:


b.to_csv('main3.csv', index=False,
          )


# In[ ]:




