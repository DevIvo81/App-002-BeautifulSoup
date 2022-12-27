import os
from pydoc import text
import re

from bs4 import BeautifulSoup
from fake_useragent import UserAgent

os.system("cls")

ua = UserAgent()
header = {'User-Agent':str(ua.chrome)}


with open("./templates/index2.html") as f:
    doc = BeautifulSoup(f, "lxml")

tags = doc.find_all("input", type="text")

for tag in tags:
    tag["placeholder"] = "I changed You!"
    
with open("./templates/changed.html", "w") as file:
    file.write(str(doc))
