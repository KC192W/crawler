from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService

from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup as bs
import pandas as pd
import time
import json
import datetime
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

#N=input('輸入號碼：')
N=166

url =f"https://api.investing.com/api/financialdata/{N}/historical/chart/?interval=PT1M&pointscount=160"
#url =f"https://api.investing.com/api/financialdata/{N}/historical/chart/?interval=P1M&pointscount=160"
driver.get(url)
driver.implicitly_wait(10)
html=driver.page_source
soup=bs(html,'lxml')
js=soup.find('pre').text.strip()
jd = json.loads(js)
df = pd.DataFrame(jd['data'])
M=str(N)+'_'+datetime.datetime.today().strftime("%Y%m%d%H")
df.to_excel(f"C:/Users/user/Desktop/{M}.xlsx", index=False,encoding="big5")

driver.close()
