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
url = f'https://www.kingstone.com.tw/search/key/{k}?'  # 替換成你要爬取的網站的 URL
driver.get(url)
html=driver.page_source
soup = bs(html, 'html.parser')
print(soup.find('div',class_="col1").find('div',class_="search_result_page").find('div',class_="searchResultHeader").find('div',class_="searchResultTitle").text.strip())
p=eval(input("查找頁數："))
data = []
for i in range(1,p+1):
    url = f"https://www.kingstone.com.tw/search/key/{k}/page/{i}"
    driver.get(url)
    html=driver.page_source
    soup = bs(html, 'html.parser')
    for index in range(0,len(soup.find_all('div',class_="division1"))):
        # 提取相應的數據
        book_title = soup.find_all('h3',class_="pdnamebox")[index].text.strip()
           

        if soup.find_all('div',class_="division1")[index].find('div',class_="basic2box").find('span',class_="author") != None:
            author=soup.find_all('div',class_="division1")[index].find('div',class_="basic2box").find('span',class_="author").text.strip()
            pb=soup.find_all('div',class_="division1")[index].find('div',class_="basic2box").find('span',class_="publish").text.strip()
            pbDate =soup.find_all('div',class_="division1")[index].find('div',class_="basic2box").find('span',class_="pubdate").text.strip()
        else:
            author=""
            pb=""
            pbDate=""        

        if len(soup.find_all('div',class_="buymixbox")[index].find_all('span'))>1:
            price = soup.find_all('div',class_="buymixbox")[index].find_all('span')[0].text.strip()
            price1 =soup.find_all('div',class_="buymixbox")[index].find_all('span')[1].text.strip()
            
        else:
            price = ""
            price1 = soup.find_all('div',class_="buymixbox")[index].find_all('span')[0].text.strip()
        a_tag =soup.find_all('h3',class_="pdnamebox")[index].find('a')
        link= "https://www.kingstone.com.tw"+a_tag.get('href')
        # 添加到表格數據中
        data.append([book_title,author,pb, pbDate, price,price1,link])
    time.sleep(random.uniform(10, 20))
driver.close()
# 創建DataFrame
df = pd.DataFrame(data, columns=["書籍標題","作者","出版社", "出版日期", "折價", "優惠價","連結"])
df.to_excel("C:/Users/user/Desktop/data1.xlsx", index=False,encoding="big5")
