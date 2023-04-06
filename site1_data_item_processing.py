#!/usr/bin/env python
# coding: utf-8

# # final

# In[2]:


import pandas as pd
import numpy as np

import operator
from operator import itemgetter, attrgetter

import matplotlib.pyplot as plt


# In[47]:


for mon in range(2,13):
    file =  pd.read_csv(f"month_final/{mon}_item.csv")
        
    cloth =[]
    total_href =[]
    total_png =[]
    total_pictime =[]
    total_loc=[]
    total_style=[]

    item_title=[]
    item_img=[]
    item_type=[]

    savefilename = f"month_final/{mon}_item_list.csv"

    for line in range(len(file)):

        input_href = file['href'][line]
        input_png = file['png'][line]
        input_pictime = file['pictime'][line]
        input_loc = file['loc'][line]
        input_style =file['style'][line]



        item = file['item'][line].split('{')[1:]
        length = len(item)
        for i in range(length):
            s = '{'+item[i]
            if i == length -1:
                s = s[:-1]
            else :
                s=s[:-2]
            d = eval(s)

            total_href.append(input_href)
            total_png.append(input_png)
            total_pictime.append(input_pictime)
            total_loc.append(input_loc)
            total_style.append(input_style)

            item_title.append(d['item_title'])
            item_img.append(d['item_img'])
            item_type.append(d['item_title'].split(" ")[-1:])

        final  = zip(total_href,total_png,total_pictime, total_loc, total_style, item_title, item_img, item_type)
        pd.DataFrame(final, columns=("href", "png","pictime","loc","style","item_title","item_img","item_type")).to_csv(savefilename)


# ## process

# In[35]:


mon = 1
file = pd.read_csv(f"month_total/mon_{mon}.csv")
cloth =[]
total_href =[]
total_png =[]
total_pictime =[]
total_loc=[]
total_style=[]

item_title=[]
item_img=[]
item_type=[]

savefilename = f"{mon}_item_list.csv"

for line in range(len(file)):
    
    input_href = file['href'][line]
    input_png = file['png'][line]
    input_pictime = file['pictime'][line]
    input_loc = file['loc'][line]
    input_style =file['style'][line]
    
    
    
    item = file['item'][line].split('{')[1:]
    length = len(item)
    for i in range(length):
        s = '{'+item[i]
        if i == length -1:
            s = s[:-1]
        else :
            s=s[:-2]
        d = eval(s)
        
        total_href.append(input_href)
        total_png.append(input_png)
        total_pictime.append(input_pictime)
        total_loc.append(input_loc)
        total_style.append(input_style)
        
        item_title.append(d['item_title'])
        item_img.append(d['item_img'])
        item_type.append(d['item_title'].split(" ")[-1:])
    
    final  = zip(total_href,total_png,total_pictime, total_loc, total_style, item_title, item_img, item_type)
    pd.DataFrame(final, columns=("href", "png","pictime","loc","style","item_title","item_img","item_type")).to_csv(savefilename)
    


# In[31]:


pd.DataFrame(final, columns=("href", "png","pictime","loc","style","item_title","item_img","item_type")).to_csv("test_zip.csv")


# In[32]:


test = pd.read_csv('test_zip.csv')


# In[33]:


test


# ### file 합쳐 진행

# In[41]:





# In[42]:


# set files path
sales1 = 'month_total/01_final_mon_1.csv'
sales2 = 'month_total/01_final_mon_2.csv'

print("*** Merging multiple csv files into a single pandas dataframe ***")

# merge files
dataFrame = pd.concat(
   map(pd.read_csv, [sales1, sales2]), ignore_index=True)
dataFrame.to_csv('month_final/1_item.csv')


# In[43]:


li = ['02','03','04','05','06','07','08','09','10','11','12']
idx = 2

for i in li:
    sales1 = f'month_total/{i}_final_mon_1.csv'
    sales2 = f'month_total/{i}_final_mon_2.csv'

    print("*** Merging multiple csv files into a single pandas dataframe ***")

    # merge files
    dataFrame = pd.concat(
       map(pd.read_csv, [sales1, sales2]), ignore_index=True)
    dataFrame.to_csv(f'month_final/{idx}_item.csv')
    idx = idx+1


# In[ ]:




