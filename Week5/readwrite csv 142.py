#!/usr/bin/env python
# coding: utf-8

# In[4]:


import csv


# In[5]:


file1=open("c:\sqlite3\csv\myfile142.txt","w")
l=["om\n","sai\n","ram\n"]


# In[6]:


file1.write("hello\n")
file1.writelines(l)
file1.close()


# In[7]:


file2=open("c:\sqlite3\csv\myfile142.txt","r")
f=file2.readlines()
print(f)


# In[ ]:




