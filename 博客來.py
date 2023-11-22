
#確認網頁內容
import requests
from bs4 import BeautifulSoup as bs
import pandas as pd
import time
import random
k=input("關鍵字：")
url = f"https://search.books.com.tw/search/query/key/{k}/cat/all"
res=requests.get(url)
soup=bs(res.text,'html.parser')
print(soup.find('div',class_="search-listbox").find('div',class_="left").find('div',class_="search_results").text.strip())

p=eval(input("查找頁數："))

data = []
for i in range(1,p+1):
    url = f"https://search.books.com.tw/search/query/key/{k}/cat/all/page/{i}"
    res=requests.get(url)
    soup=bs(res.text,'html.parser')
    
    if len(soup.find_all('h4'))>=55:
        m=55
    else:
        m=len(soup.find_all('h4'))-6
    
    for index in range(1,m):
        # 提取相應的數據
        book_title = soup.find_all('h4')[index].text.strip()
        author = soup.find_all('p', class_='author')[index-1].text.strip()
        price = soup.find_all('li')[index+3].text.strip()
        a_tag = soup.find_all('a', target="_blank")[index*2-1]
        link="https:"+a_tag.get('href')
        # 添加到表格數據中
        data.append([book_title, author, price,link])
    time.sleep(random.uniform(10, 20))
# 創建DataFrame
df = pd.DataFrame(data, columns=["書籍標題", "作者", "價格","連結"])
df.to_excel("C:/Users/user/Desktop/data1.xlsx", index=False,encoding="big5")