import requests
import pandas as pd
import xmltodict
url="https://emap.pcsc.com.tw/EMapSDK.aspx"
payload={
    'searchType': 'ShopList',
    'type': '',
    'city': '新北市',
    'area': '新莊區',
    'road': '',
    'fun': 'showStoreList',
    'key': '6F30E8BF706D653965BDE302661D1241F8BE9EBC'

}
res=requests.get(url,params=payload)
print(res)
jd=xmltodict.parse(res.text)

const puppeteer = require('puppeteer');

(async () => {
    const browser = await puppeteer.launch();
    const page = await browser.newPage();
    await page.goto('https://api.map.com.tw/net/familyShop.aspx?searchType=ShopList&type=&city=%E5%8F%B0%E5%8C%97%E5%B8%82&area=%E4%B8%AD%E6%AD%A3%E5%8D%80&road=&fun=showStoreList&key=6F30E8BF706D653965BDE302661D1241F8BE9EBC');
    // 在页面上执行JavaScript
    const title = await page.evaluate(() => document.title);
    console.log(title);
    await browser.close();
})();