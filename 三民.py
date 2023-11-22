
#確認網頁內容
import requests
from bs4 import BeautifulSoup as bs
import pandas as pd
import time
import random
k=input("關鍵字：")
url = f"https://www.sanmin.com.tw/search/index/?ct=k&qu={k}"
res=requests.get(url)
soup=bs(res.text,'html.parser')
print(soup.find_all("div",class_="PageNumBar")[0].find_all("li")[2].text.strip())
p=eval(input("查找頁數："))

data = []
for i in range(1,p+1):
    url = f"https://www.sanmin.com.tw/search/index?ct=k&k={k}&pi={i}"
    res=requests.get(url)
    soup=bs(res.text,'html.parser')
  
    for index in range(1,len(soup.find_all('h3',class_="Title"))+1):
        # 提取相應的數據
        book_title = soup.find_all('h3',class_="Title")[index-1].text.strip()
        author=soup.find_all('div',class_="Author")[index-1].find_all('span')[1].text.strip()
        pb=soup.find_all('div',class_="Author")[index-1].find_all('span')[3].text.strip()
        pbDate = soup.find_all('div',class_="Author")[index-1].find_all('span')[4].text.strip()
        if len(soup.find_all('div',class_="lh-30")[index-1].find_all('span')) !=0:
            price = soup.find_all('div',class_="lh-30")[index-1].find_all('span')[0].find_all('span')[0].text.strip()
            price1 =soup.find_all('div',class_="lh-30")[index-1].find_all('span')[0].find_all('span')[1].find_all('span')[2].text.strip()
            
        else:
            price = soup.find_all('div',class_="lh-30")[index-1].find_all('a')[0].text.strip()
            price1 = ""
        a_tag =soup.find_all('h3',class_="Title")[index-1].find_all('a')[0]
        link= "https://www.sanmin.com.tw"+a_tag.get('href')
        # 添加到表格數據中
        data.append([book_title,author,pb, pbDate, price,price1,link])
    time.sleep(random.uniform(10, 20))

# 創建DataFrame
df = pd.DataFrame(data, columns=["書籍標題","作者","出版社", "出版日期", "定價", "優惠價","連結"])
df.to_excel("C:/Users/user/Desktop/data1.xlsx", index=False,encoding="big5")