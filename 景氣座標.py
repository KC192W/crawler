from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import time
import pandas as pd
# 指定瀏覽器驅動程式的路徑

chrome_options = webdriver.ChromeOptions()
#chrome_options.add_argument('--headless')
chrome_options.add_argument('--window-size=1200x600')
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=chrome_options)

paths_data = []
url = 'https://www.macromicro.me/charts/64/econ-cycle'
driver.get(url)
paths_data = []

# 隱式等待，最長等待時間為10秒
driver.implicitly_wait(10)

# 等待元素加載
#time.sleep(5)  # 或者使用隱式等待等待特定元素的加載


# 收集動態生成的內容
for _ in range(10):  # 假設這裡你想收集 10 次更新
    # 獲取網頁內容
    page_source = driver.page_source

    # 使用 BeautifulSoup 解析 HTML
    soup = BeautifulSoup(page_source, 'html.parser')

    # 找到並提取 <path> 元素
    path_element=soup.find('g',class_="highcharts-series highcharts-series-1 highcharts-scatter-series").find('path',class_='highcharts-graph')
    #path_element=soup.find('g',class_="highcharts-markers highcharts-series-1 highcharts-scatter-series").find('path',class_="highcharts-point")

    # 如果找到 path 元素，提取 d 屬性的值
    Dat=soup.find('text',class_="highcharts-subtitle").text.strip()
     # 將資料添加到列表中
    paths_data.append([Dat,path_element.get('d')])

    # 休眠一段時間，等待下一次更新
    time.sleep(0.3)


# 關閉瀏覽器
#driver.quit()
df = pd.DataFrame(paths_data, columns=["月份","座標"])
df.to_excel("C:/Users/user/Desktop/data1.xlsx", index=False,encoding="big5")