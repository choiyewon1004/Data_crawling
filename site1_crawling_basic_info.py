# -*- coding: utf-8 -*-
"""1.crawling_basic_info.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1oqvA3Yzy2UWN4byo4_lBIa3Z-rru91aG

# 옷 스타일별 크롤링

## 촬영날짜, 게시날짜 정확히
"""

from bs4 import BeautifulSoup
import requests
import pandas as pd
from tqdm.auto import tqdm

result_href =[]
result_png =[]
result_pictime=[]
result_place =[]

crawl_list = ['americancasual','casual','chic','dandy','formal','girlish','golf','homewear','retro','romantic','sports','street','gorpcore']

def geturl(url):
    response = requests.get(url)
    html = BeautifulSoup(response.content, 'html.parser')
    return html

for i in tqdm(crawl_list, leave=True, desc=f"{i}"):
    url = "https://www.musinsa.com/mz/streetsnap?style_type="+i
    html = geturl(url).find_all("div",{"class":"articleImg"})
    for board in tqdm(html, leave= True):
        move_url = "https://www.musinsa.com"+board.find('a')['href']
        result_href.append(move_url)
        find_list = board.select('img')
        find_pictime = geturl(move_url).select('table>tbody>tr>td>span')[1].get_text()
        result_pictime.append(find_pictime)
        for j in find_list:
            result_place.append(j['alt'].split('_')[0])
            result_png.append(j['src'])
            
final_df = pd.DataFrame(zip(result_href, result_png, result_pictime, result_place), columns=['href','png','pictime','place'])

final_df

final_df.to_csv("result1.csv", mode='w')

"""## 촬영 날짜, 게시 날짜 동일 시

"""

result2_href =[]
result2_png =[]
result2_pictime=[]
result2_place =[]

for url in tqdm(crawl_list, leave=True):
    html = geturl(url).find_all("div",{"class":"articleImg"})
    for board in tqdm(html, leave= True):
        move_url = "https://www.musinsa.com"+board.find('a')['href']
        result2_href.append(move_url)
        find_list = board.select('img')
        find_pictime = geturl(move_url).select('table>tbody>tr>td>span')[1].get_text()
        result2_pictime.append(find_pictime)
        for j in find_list:
            result2_place.append(j['alt'].split('_')[0])
            result2_png.append(j['src'])
            
    html = geturl(url).find_all("div",{"class":"articleInfo"})
    for board in tqdm(html, leave=True):
        result2_pictime.append(board.select('span',{"class":"division"})[1].get_text())
            
final2_df = pd.DataFrame(zip(result2_href, result2_png, result2_pictime, result2_place), columns=['href','png','pictime','place'])

final2_df.to_csv("result2.csv", mode='w')









