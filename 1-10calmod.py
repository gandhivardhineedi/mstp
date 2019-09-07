#!/usr/bin/env python
# coding: utf-8

# In[5]:


def add(a,b):
    return a+b


# In[4]:


def sub(a,b):
    return a-b


# In[6]:


def mul(a,b):
    return a*b


# In[13]:


def div(a,b):
    try:
        return(a//b,a%b)
    except(ZeroDivisionError):
        print('divide by zero')


# In[ ]:





# In[ ]:




