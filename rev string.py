#!/usr/bin/env python
# coding: utf-8

# In[3]:


S=input("Enter a string: ")
l=len(S)
for i in range(l-1,-1,-1):
    print(S[i],end="")

