from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup as bs
import pandas as pd
import json
'''
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=chrome_options)
'''
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
k=input("關鍵字:")
url=f"https://rtapi.ruten.com.tw/api/rtb/v1/index.php/core/prod?q={k}&type=direct&sort=rnk%2Fdc&limit=200&offset=1"
driver.get(url)
res=driver.page_source
soup = bs(res, 'html.parser')
script_tag = soup.find('pre').text.strip()
json_content = json.loads(script_tag)

df=pd.DataFrame(json_content["Rows"])
i =','.join(df['Id'].astype(str))

url2="https://rtapi.ruten.com.tw/api/prod/v2/index.php/prod?id=" + i
driver.get(url2)
res2= driver.page_source
driver.close()

soup2 = bs(res2, 'html.parser')
script_tag = soup2.find('pre').text.strip()
json_content2 = json.loads(script_tag)
df2=pd.DataFrame(json_content2)
df2["ProdId"] = df2["ProdId"].apply(lambda x: f"https://www.ruten.com.tw/item/show?{x}")
sd=pd.DataFrame(df2.iloc[:, [0, 1, 6]])
sd.to_excel(f"C:/Users/user/Desktop/{k}.xlsx", index=False, encoding="big5")






