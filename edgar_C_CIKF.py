from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
#from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup as bs
import pandas as pd
import time

df2=pd.DataFrame()
C=pd.read_csv('C:/Users/user/Desktop/公司名.csv')
driver = webdriver.Chrome(service=ChromeService(
    ChromeDriverManager().install()))

url =f"https://www.sec.gov/edgar/search/#/dateRange=all&entityName=FINANCIAL"
driver.get(url)
driver.implicitly_wait(10)
htmla=driver.page_source
soupa = bs(htmla, 'lxml')
if soupa.find('a',id='show-full-search-form') != None:
    element = driver.find_element(By.ID,'show-full-search-form')
    driver.execute_script("arguments[0].click();", element)
    driver.implicitly_wait(10)

for cn in C.iloc[:, 0]:
    
    url =f"https://www.sec.gov/edgar/search/#/dateRange=all&entityName={cn}"
    driver.get(url)
    driver.implicitly_wait(4)
    
    element1 = driver.find_element(By.ID,'keywords')
    driver.execute_script("arguments[0].click();", element1)
    time.sleep(4)
    element1.send_keys(Keys.TAB)
    time.sleep(5)
    html=driver.page_source
    soup = bs(html, 'lxml')
    tb=soup.find('table',id="asdf")
    
    if tb.text.strip() != "":
        rows = soup.find_all('tr', class_='hint')
        data = []
        for row in rows:
            entity = row.find('td', class_='hint-entity').text.strip()
            cik = row.find('td', class_='hint-cik').find('i').text.strip()
            data.append({'公司名稱': entity, 'CIK': cik})
        df = pd.DataFrame(data)
        if df.shape[0] !=0:
            df.insert(0,'查詢名稱', cn)
            df2 = pd.concat([df2,df], ignore_index=True)
            df=pd.DataFrame()
        else:
            df=pd.DataFrame({'查詢名稱': [cn], '公司名稱': ['無此公司'], 'CIK': ['']})
            df2 = pd.concat([df2,df], ignore_index=True)
            df=pd.DataFrame()
    else:
        df=pd.DataFrame({'查詢名稱': [cn], '公司名稱': ['請重新查詢'], 'CIK': ['']})
        df2 = pd.concat([df2,df], ignore_index=True)
        df=pd.DataFrame()

df2.to_excel(f"C:/Users/user/Desktop/查詢名稱1.xlsx", index=False,encoding="big5")

driver.close()