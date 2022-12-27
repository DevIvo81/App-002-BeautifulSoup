import requests
import os

from bs4 import BeautifulSoup
from fake_useragent import UserAgent

os.system("cls")

ua = UserAgent()
header = {'User-Agent':str(ua.chrome)}


url = 'https://coinmarketcap.com'
result = requests.get(url, headers=header).text
doc = BeautifulSoup(result, "html.parser")

tbody = doc.tbody
trs = tbody.contents

prices = {}

for tr in trs[:10]:
    name, price = tr.contents[2:4]
    fixed_name = name.p.string
    fixed_price = price.a.string
    prices[fixed_name] = fixed_price

print(prices)