from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup as bs
import time
import random
import pandas as pd
driver = webdriver.Chrome(service=ChromeService(
    ChromeDriverManager().install()))

k=input("關鍵字：")
url = f'https://www.momoshop.com.tw/search/searchShop.jsp?keyword={k}&searchType=1&curPage=1&_isFuzzy=0&showType=chessboardType&isBrandCategory=N&serviceCode=MT01'  # 替換成你要爬取的網站的 URL
driver.get(url)
html=driver.page_source


soup = bs(html, 'html.parser')
p=eval(input("查找頁數："))

data = []
for i in range(1,p+1):
    url = f"https://www.momoshop.com.tw/search/searchShop.jsp?keyword={k}&searchType=1&curPage={i}&_isFuzzy=0&showType=chessboardType&isBrandCategory=N&serviceCode=MT01"
    driver.get(url)
    html=driver.page_source
    soup = bs(html, 'html.parser')
    for index in range(0,len(soup.find_all('a',class_="goodsUrl"))):
        # 提取相應的數據
        title = soup.find('div',class_="BodyBase").find('div',class_="bt_2_layout searchbox searchListArea selectedtop").find('div',class_="searchPrdListArea bookList").find('div',class_="listArea").find_all('h3',class_="prdName")[index].text.strip()
        price=soup.find('div',class_="BodyBase").find('div',class_="bt_2_layout searchbox searchListArea selectedtop").find('div',class_="searchPrdListArea bookList").find('div',class_="listArea").find_all('p',class_="money")[index].find('span',class_="price")
        a_tag =soup.find_all('a',class_="goodsUrl")[index]
        link= "https://www.kingstone.com.tw"+a_tag.get('href')
        # 添加到表格數據中
        data.append([title,price,link])
    time.sleep(random.uniform(10, 20))
driver.close()
# 創建DataFrame
df = pd.DataFrame(data, columns=["標題","價格","連結"])
df.to_excel("C:/Users/user/Desktop/data1.xlsx", index=False,encoding="big5")
