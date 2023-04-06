
import pandas as pd
import numpy as np

import operator
from operator import itemgetter, attrgetter

import matplotlib.pyplot as plt



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
            tit = str(d['item_title'].split(" ")[-1:])
            tit = tit.replace("\'","").replace("[","").replace("]","")
            
            
            total_href.append(input_href)
            total_png.append(input_png)
            total_pictime.append(input_pictime)
            total_loc.append(input_loc)
            total_style.append(input_style)

            item_title.append(d['item_title'])
            item_img.append(d['item_img'])
            item_type.append(tit)

        final  = zip(total_href,total_png,total_pictime, total_loc, total_style, item_title, item_img, item_type)
        pd.DataFrame(final, columns=("href", "png","pictime","loc","style","item_title","item_img","item_type")).to_csv(savefilename)


