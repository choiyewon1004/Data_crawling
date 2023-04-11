
import pandas as pd
import numpy as np
import warnings
warnings.filterwarnings(action='ignore')


def pro(tit):
    # 바지 처리
    if (tit != '카고팬츠') and ('팬츠' in tit):
        if tit == '데님팬츠' :
            tit = '청바지'
        if (mon < 5 or mon>9):
            tit = '긴바지'
        if (mon>=5 and mon <10):
            tit = '반바지'
    if tit =='슬랙스':
        tit = '긴바지'

    # 티셔츠 처리
    if '티셔츠' in tit:
        if (mon < 5 or mon>9):
            tit = '긴팔'
        if (mon>=5 and mon <10):
            tit = '반팔'
            
    # 반팔 처리
    if '나시' in tit or '크롭' in tit : 
        tit = '반팔'
        
    # 반바지
    if '쇼츠' in tit :
        tit = '반바지'
        
    # 부츠 처리
    if  '부츠' in tit :
        tit = '부츠'

    # 패딩 처리
    if  ('패딩' in tit ) or ('파카' in tit) or ('아우터' in tit) or ('구스다운' in tit):
        tit = '패딩'

     # 재킷 처리
    if  ('재킷' in tit ) or ('블레이저' in tit) or ('자켓' in tit) :
        tit = '재킷'

    # 코트 처리
    if  '코트' in tit :
        tit = '코트'

    # 점퍼 처리
    if  ('점퍼' in tit) or ('집업' in tit) :
        tit = '점퍼'

    # 스커트 처리
    if  '스커트' in tit :
        tit = '스커트'

    # 셔츠 처리
    if  '스웨트' in tit :
        tit = '스웨터'

     # 후디 처리
    if  '후디' in tit or '후드' in tit :
        tit = '긴팔'   
    
    # 가디건 처리
    if '카디건' in tit :
        tit = '가디건'
        
    # 와이셔츠 처리
    if '와이셔츠' in tit or '셔츠' in tit :
        tit = '셔츠'   
    
    if '워커' in tit:
        tit = '워커'
        
    return tit



for mon in range(12,13):
  file =  pd.read_csv(f"month_final/{mon}_item.csv")
  
  final_df = pd.DataFrame(columns =['mon','png','반팔','긴팔','스웨터','셔츠','블라우스','원피스','니트','가디건','폴로셔츠','점퍼','재킷','코트','패딩','청바지','긴바지','반바지','스커트','카고팬츠','구두','운동화','스니커즈','샌들','워커','부츠'] )
  item_list_up = ['반팔','긴팔','스웨터','셔츠','블라우스','원피스','니트','가디건','폴로셔츠','점퍼','재킷','코트','패딩','청바지','긴바지','반바지','스커트','카고팬츠','구두','운동화','스니커즈','샌들','워커','부츠']
  savefilename = f"month_category/{mon}_category.csv"

  for line in range(0,len(file)):
      append_li = [mon , file['png'][line]]

      item = file['item'][line].split('{')[1:]
      length = len(item)

      item_list = []
      for i in range(length):

          s = '{'+item[i]
          if i == length -1:
              s = s[:-1]
          else :
              s=s[:-2]

          d = eval(s)

          tit = str(d['item_title'].split(" ")[-1:]).replace("\'","").replace("[","").replace("]","")           
          
          if tit == '스타일':
              s = str(d['item_title'].split(" ")[-3:-2]).replace("\'","")
              s = s.replace("[","").replace("]","")
              tit = s[:-1]
              tit = tit.replace("\'","").replace("[","").replace("]","")
          tit = pro(tit).replace('.','')
          
          
          
          item_list.append(tit)

      for i in item_list_up: 
          if i in item_list:
              append_li.append(1)
          else : 
              append_li.append(0)
      
      for i in item_list :
          if i not in item_list_up:
              print(i)
              
      final_df = final_df.append(pd.Series(append_li, index=final_df.columns), ignore_index=True)
      print("*"*90)
  final_df.to_csv(savefilename)
  
