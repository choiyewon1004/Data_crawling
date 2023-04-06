#!/usr/bin/env python
# coding: utf-8

# # final

# In[55]:


import pandas as pd
import numpy as np

import operator
from operator import itemgetter, attrgetter

import matplotlib.pyplot as plt


# In[9]:


def count_frequency(my_list):
    
    count = {}
    
    for item in my_list:
        count[item] = count.get(item, 0) + 1
        
    return count


# In[4]:


def findstyle(file):
    file = pd.read_csv(file)
    cloth =[]
    
    for line in range(len(file)):
        # clo_sty = file['style'][line]
        item = file['item'][line].split('{')[1:]
        length = len(item)

        for i in range(length):
            s = '{'+item[i]
            if i == length -1:
                s = s[:-1]
            else :
                s=s[:-2]

            d = eval(s)
            cloth.extend(d['item_style'])    
    return cloth


# In[87]:


for i in range(1,13):
    result = []
    li_1 = findstyle(f"mon_{i}.csv")
    li_2 = findstyle(f"2_final_mon_{i}.csv")
    result.extend(li_1)
    result.extend(li_2)
    count = count_frequency(result)
    #print(count)
    
    count_order = sorted(
        count.items(),
        key= operator.itemgetter(1),
        reverse = True
    )
    #print(count_order)
    
    li_color_name =[]
    li_color_count = []

    li = list(count.keys())
    for ki in range(len(li)):
        if '색' in li[ki]:
            if li[ki] =='검정색' or li[ki]=='검정' : 
                continue
            li_color_name.append(li[ki])
            color_count =0
            for kj in range(len(li)):
                if li[ki][:-1] in li[kj]:
                    color_count += count[li[kj]]
            li_color_count.append(color_count)
    
    plt.figure(figsize=(15,6))
    plt.rcParams['font.family'] ='Malgun Gothic'
    plt.title(f'month[{i}] color')
    plt.bar(li_color_name, li_color_count, width=0.5)
    plt.xlabel('color')
    plt.ylabel('cnt')
    plt.show()

  


# # Process

# In[26]:


import pandas as pd
import numpy as np


# In[88]:


file = pd.read_csv('mon_1.csv')


# In[138]:


cloth =[]


# In[136]:


cloth=[]
for line in range(2):
    clo_sty = file['style'][line]
    item = file['item'][line].split('{')[1:]
    length = len(item)
    result =[]
    
    for i in range(length):
        s = '{'+item[i]
        if i == length -1:
            s = s[:-1]
        else :
            s=s[:-2]
       
        d = eval(s)
        print(d)
        cloth.extend(d['item_style'])    


# In[137]:


cloth


# ---

# In[122]:


for line in range(2):
    clo_sty = file['style'][line]
    item = file['item'][line].split('{')[1:]
    length = len(item)
    result =[]
    
    for i in range(length):
        s = '{'+item[i]
        if i == length -1:
            s = s[:-1]
        else :
            s=s[:-2]
       
        d = eval(s)
        print()
        print(d['item_style'])
        
    print()
    print()
    print()
    


# In[ ]:





# In[153]:


for mon in range(1,13):
    file1 = pd.read_csv(f'mon_{mon}.csv')
    cloth =[]
    
    for line in range(len(file)):
        # clo_sty = file['style'][line]
        item = file['item'][line].split('{')[1:]
        length = len(item)

        for i in range(length):
            s = '{'+item[i]
            if i == length -1:
                s = s[:-1]
            else :
                s=s[:-2]

            d = eval(s)
            cloth.extend(d['item_style'])    

    print(f"{mon}월 스타일 ")
    print(set(cloth))
    


# In[50]:


li_color_name =[]
li_color_count = []

li = list(count.keys())
for i in range(len(li)):
    if '색' in li[i]:
        li_color_name.append(li[i])
        color_count =0
        #print(li[i] , ":" , count[li[i]])
        for j in range(len(li)):
            if li[i][:-1] in li[j]:
                #print(">",li[j] , ":" , count[li[j]])
                color_count += count[li[j]]
        #print("color_count ", color_count)
        li_color_count.append(color_count)

