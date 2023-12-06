from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup as bs
import re
import pandas as pd
import time
import random
SIC=input("SIC:")
fl=input("Filings:")
driver = webdriver.Chrome(service=ChromeService(
    ChromeDriverManager().install()))
data=pd.DataFrame()
df2=pd.DataFrame()
a_href_list=[]
L=100
i=0
while L == 100 :
    c=i*100
    i+=1
    url =f"https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&SIC={SIC}&owner=include&match=starts-with&start={c}&count=100&hidefilings=0"
    driver.get(url)
    html=driver.page_source
    soup = bs(html, 'lxml')
    if soup.find("table")!=None:
        tb=soup.select("table")[0]
        df=pd.read_html(str(tb),header=[0])[0]
        L=df.shape[0]
        
        for index in range(90, L):
            content = str(df.iloc[index, 0])
            company = str(df.iloc[index, 1])
            state = str(df.iloc[index, 2])
            # Use BeautifulSoup to extract the 'href' attribute
            href = soup.find('table', class_='tableFile2').find_all('tr')[index+1].find_all('a')[0]['href']
            # href = df.iloc[index, 0].find('a')['href']
            driver.get(f"https://www.sec.gov{href}&type={fl}")
            html2 = driver.page_source
            soup2 = bs(html2, 'lxml')
            if soup2.find("table")!=None:
                tb2 = soup2.find("table",class_="tableFile2")
                
                if len(tb2.find_all('a', id="documentsbutton"))!=0:
                    f=soup2.find('div',id="contentDiv").find('div').find_all('div')[1].text.strip()
                    f = re.sub('Business Address','', f)
                    f= ' '.join(f.split())
                    print(f)
                    for s in range(0,len(tb2.find_all('a', id="documentsbutton"))):
                        a_href_list.append("https://www.sec.gov"+tb2.find_all('a',id="documentsbutton")[s]['href'])
                    
                    df2 = pd.read_html(str(tb2), header=[0])[0]
                    df2.insert(0, 'documentslink', a_href_list)

                    filtered_df = df2[df2['Filings'] == fl]        
                    
                    filtered_df.insert(0,'Companylink',f"https://www.sec.gov{href}")
                    filtered_df.insert(0,'Business Address',f)
                    filtered_df.insert(0,'State/Country', state)
                    filtered_df.insert(0,'CIK', content)
                    filtered_df.insert(0,'Company', company)
        
                    
                    data = pd.concat([data, filtered_df], ignore_index=True)
                a_href_list=[]
                #time.sleep(random.uniform(1,5))
    L=99
N="SIC："+SIC+"CIK"
data.to_excel(f"C:/Users/user/Desktop/{N}.xlsx", index=False,encoding="big5")
driver.close()