# -*- coding: utf-8 -*-
"""final_crawling.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/15zHRMdY7aaP8pPUCvYvAavvE8iR_FZGe
"""

from bs4 import BeautifulSoup
import requests
import pandas as pd
from tqdm.auto import tqdm


#find_url = "https://www.musinsa.com/mz/streetsnap?_mon="


def geturl(url):
    response = requests.get(url)
    html = BeautifulSoup(response.content, 'html.parser')
    return html


for mon in tqdm(range(5,13), leave=True):
  result_href =[]
  result_png =[]
  result_pictime=[]
  result_loc =[]
  result_style=[]
  result_item=[]

  filename = f"mon_{mon}.csv"
  for page in range(1,3):
    url = f"https://www.musinsa.com/mz/streetsnap?_mon={mon}&gender=&p={page}#listStart"

    html = geturl(url).find_all("div",{"class":"articleImg"})
    for board in tqdm(html, leave= True):
      move_url = "https://www.musinsa.com"+board.find('a')['href']
      result_href.append(move_url)

      move_html = geturl(move_url)
      find_info = move_html.select('table>tbody>tr')
      for i in find_info:
        find_info_title = i.find("span")
        if find_info_title.get_text() == "촬영일":
          #print("촬영일 : ",i.select_one("tr>td>span").get_text() ) /
          result_pictime.append(i.select_one("tr>td>span").get_text())
        elif find_info_title.get_text() == "촬영지역":
          #print("촬영지역 : ",i.select_one("tr>td>span").get_text()) 
          result_loc.append(i.select_one("tr>td>span").get_text()) 
        elif find_info_title.get_text() == "스타일":
          #print("스타일 : ",i.select_one("tr>td>span").get_text()) 
          result_style.append(i.select_one("tr>td>span").get_text())

      result_png.append(move_html.find("div",{"class": "snapImg"}).find('a')['href'])

      check_item =[]
      find_clothes = move_html.find("ul", {"class":"styleItem-list"}).find_all("div",{"class" : "itemImg"})

      for i in find_clothes:
        res_dic={}
        style_list=[]
        find_clothes_title = i.find("p",{"class" : "title"}).get_text().replace("\t","")[1:]
        find_clothes_style = i.find_all('span')
        for j in find_clothes_style:
            style_list.append(j.get_text())
        res_dic['item_title'] = find_clothes_title
        res_dic['item_img'] = i.find('a')['href']
        res_dic['item_style'] = style_list
        
        check_item.append(res_dic)
      result_item.append(check_item)
      
  final_df = pd.DataFrame(zip(result_href, result_png, result_pictime, result_loc,result_style, result_item), columns=['href','png','pictime','loc', 'style','item'])   
  final_df.to_csv(filename)

