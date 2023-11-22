
#確認網頁內容
import requests
from bs4 import BeautifulSoup as bs
import pandas as pd
import time
import random
k=input("關鍵字：")
url = f"https://www.tenlong.com.tw/search?utf8=%E2%9C%93&keyword={k}"
res=requests.get(url)
soup=bs(res.text,'html.parser')
if len(soup.find_all('a',rel="next")) != 0:
    print("最多搜尋頁數：",soup.find_all('a')[-7].text.strip(),"頁")
    p=eval(input("查找頁數："))
else:
    print("最多搜尋頁數： 1 頁")
    p=1

data = []
for i in range(1,p+1):
    url = f"https://www.tenlong.com.tw/search?utf8=%E2%9C%93&keyword={k}&page={i}"
    res=requests.get(url)
    soup=bs(res.text,'html.parser')
    for index in range(1,len(soup.find_all('div',class_="book-data"))+1):
        # 提取相應的數據
        book_title = soup.find_all('strong',class_="")[index-1].text.strip()
        pbDate = soup.find_all('span',class_="publish-date")[index-1].text.strip()
        price = soup.find_all('span',class_="price")[index-1].text.strip()
        a_tag =soup.find_all('a',class_="cover w-full")[index-1]
        link= "https://www.tenlong.com.tw"+a_tag.get('href')
        # 添加到表格數據中
        data.append([book_title, pbDate, price,link])
    time.sleep(random.uniform(10, 20))

# 創建DataFrame
df = pd.DataFrame(data, columns=["書籍標題", "出版日期", "價格","連結"])
df.to_excel("C:/Users/user/Desktop/data1.xlsx", index=False,encoding="big5")
