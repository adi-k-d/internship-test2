#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# In[2]:


df=pd.read_csv('main.csv')


# In[3]:


df


# In[4]:


a=df.groupby((df.Year//10)*10).sum()
a


# In[5]:


a.drop(['Year'], axis=1)


# In[7]:


a.to_csv('main1.csv',index=False)


# In[ ]:




