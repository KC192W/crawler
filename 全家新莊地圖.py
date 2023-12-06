"""
!pip install folium
!pip install geocoder
"""
import requests
import pandas as pd
import re
import json
import folium
import geocoder
url="https://api.map.com.tw/net/familyShop.aspx"
headers={
    'Referer':'https://www.family.com.tw/',
}
payload={
    'searchType': 'ShopList',
    'type': '',
    'city': '新北市',
    'area': '新莊區',
    'road': '',
    'fun': 'showStoreList',
    'key': '6F30E8BF706D653965BDE302661D1241F8BE9EBC'

}
res=requests.post(url,params=payload,headers=headers)


cleaned_content = re.sub(b'\s+', b'', res.content)

match = re.search(b'showStoreList\((.*)\)', cleaned_content)

jd = json.loads(match.group(1))
df = pd.DataFrame(jd)
location=geocoder.osm("新北市").latlng
m=folium.Map(location=location,zoom_start=15)
for item in df.values:
    folium.Marker(location=[item[4],item[3]],popup=item[0]).add_to(m)
    folium.Marker(location=[25.0363219,121.43008],
                  popup="輔大",
                  icon=folium.Icon(
                  icon='info-sign',
                  color='red')).add_to(m)
                  
print(m)
