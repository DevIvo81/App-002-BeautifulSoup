import requests
import os

from bs4 import BeautifulSoup
from fake_useragent import UserAgent

os.system("cls")

ua = UserAgent()
header = {'User-Agent':str(ua.chrome)}


url = 'https://www.nasdaq.com/market-activity/currencies'
result = requests.get(url, headers=header).text
doc = BeautifulSoup(result, "html.parser")

currencies = {}

tbody = doc.tbody
print(tbody)


print(currencies)