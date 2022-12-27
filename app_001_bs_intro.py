import requests
import os

from bs4 import BeautifulSoup
from fake_useragent import UserAgent

os.system("cls")

ua = UserAgent()
header = {'User-Agent':str(ua.chrome)}


url = 'https://www.newegg.com/gigabyte-geforce-rtx-3080-gv-n3080gaming-oc-10gd/p/N82E16814932329'

result = requests.get(url, headers=header)
doc = BeautifulSoup(result.text, "html.parser")

prices = doc.find_all(text="$")

parent = prices[0].parent

print(parent)

strong = parent.find("strong")
print(strong.string)
