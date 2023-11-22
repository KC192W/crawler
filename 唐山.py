
#確認網頁內容
import requests
from bs4 import BeautifulSoup as bs
import pandas as pd
import math
import time
import random
k=input("關鍵字：")
url = f"https://tonsanbookstore.cyberbiz.co/search?q={k}&page=1"
res=requests.get(url)
soup=bs(res.text,'html.parser')
t=eval(soup.find_all('strong')[0].text.strip())
t=math.ceil(t/24)
print(soup.find_all('h5')[0].text.strip(),"，共",t,"頁",sep=" ")

p=eval(input("查找頁數："))
data = []
for i in range(1,p+1):
    url = f"https://tonsanbookstore.cyberbiz.co/search?q={k}&page={i}"
    res=requests.get(url)
    soup=bs(res.text,'html.parser')
    
    for index in range(1,len(soup.find_all('div', class_='product_price'))+1):
        # 提取相應的數據
        book_title = soup.find_all('div')[41+index*7].text.strip()
        price = soup.find_all('div', class_='product_price')[index-1]
        price = price.text.strip().replace('<del>', '').replace('</del>', '').replace('\n', ',原價：')
        t = soup.find_all('a', class_='productClick img-flex GTM-info')[index-1]
        t_b=t['data-brand']
        t_c=t['data-category']
        link="https://tonsanbookstore.cyberbiz.co"+t.get('href')
        # 添加到表格數據中
        data.append([book_title, price,t_b,t_c,link])
    time.sleep(random.uniform(10, 20))
# 創建DataFrame
df = pd.DataFrame(data, columns=["書籍標題", "價格","出版社","書籍類別","連結"])
df.to_excel("C:/Users/user/Desktop/data1.xlsx", index=False,encoding="big5")

