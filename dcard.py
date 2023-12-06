
import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup as bs
import time
driver = webdriver.Chrome(service=ChromeService(
    ChromeDriverManager().install()))

driver.get("https://www.dcard.tw/f/horoscopes")
driver.implicitly_wait(10)
time.sleep(3)
html=driver.page_source

soup = bs(html, 'html.parser')
driver.close()

for i in range(0,len(soup.find_all('div',class_='atm_d2_1gzgpud atm_ks_15vqwwr m16n7y82'))):
   f=soup.find_all('h2')[i].text.strip()
   t=soup.find_all('div',class_='atm_d2_1gzgpud atm_ks_15vqwwr m16n7y82')[i].text.strip()
   print("*"+f)
   print("  描述："+t)
   

