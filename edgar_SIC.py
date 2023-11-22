from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup as bs
import pandas as pd
SIC=input("SIC:")
driver = webdriver.Chrome(service=ChromeService(
    ChromeDriverManager().install()))
datalist=[]
L=100
i=0
while L == 100 :
    c=i*100
    i+=1
    url =f"https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&SIC={SIC}&owner=include&match=starts-with&start={c}&count=100&hidefilings=0"
    driver.get(url)
    html=driver.page_source
    soup = bs(html, 'lxml')
    tb=soup.select("table")
    df=pd.read_html(tb[0].prettify(),header=[0])[0]
    L=df.shape[0]
    datalist.append(df)
df0 = pd.concat(datalist, ignore_index=True)
N="SIC："+SIC
df0.to_excel(f"C:/Users/user/Desktop/{N}.xlsx", index=False,encoding="big5")
driver.close()