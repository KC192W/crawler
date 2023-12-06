from bs4 import BeautifulSoup

html_content = '''
<div class="product_image">
  <a class="productClick img-flex GTM-info"
    href="/products/9789578019676"
    data-brand="前衛"
    data-category="台灣史"
    data-collection_id=""
    data-id="34308640"
    data-list=""
    data-name="零下六十八度：二戰後臺灣人的西伯利亞戰俘經驗"
    data-position="13"
    data-price="298.0">
    <img class="img-lazy"
         src="//cdn1-next.cybassets.com/s/files/15130/theme/48017/assets/img/1630562752_7826d93e_img_loading.svg?1630562752"
         data-src="//cdn1-next.cybassets.com/media/W1siZiIsIjE1MTMwL3Byb2R1Y3RzLzM0MzA4NjQwLzE2Mjk0Mzg1NDVfNGNhMDI2NzdjNjA3MzIwMTc4MTcucG5nIl0sWyJwIiwidGh1bWIiLCI2MDB4NjAwIl1d.png?sha=e09675dbbe7422e1"
         alt="product_image"
         width="250"
         height="250">
    <div class="swiper-lazy-preloader-white"></div>
  </a>
</div>
'''

soup = BeautifulSoup(html_content, 'html.parser')

# 找到具有特定 data-category 值的元素
target_element = soup.find('div', {'data-category': '台灣史'})

# 提取 data-category 屬性的值
if target_element:
    category_value = target_element['data-category']
    print(category_value)
else:
    print("未找到符合條件的元素")
    
#############
price = soup.find_all('div', class_='product_price')[index-1].text.strip()
# 添加到表格數據中
data.append([book_title, price])

# 創建DataFrame
df = pd.DataFrame(data, columns=["書籍標題", "價格"])
df.to_excel("C:/Users/user/Desktop/data1.xlsx", index=False,encoding="big5")