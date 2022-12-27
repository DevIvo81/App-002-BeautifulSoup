from flask import Flask, jsonify
import requests
import os
import re

from bs4 import BeautifulSoup
from fake_useragent import UserAgent

# os.system("cls")

def gradovi():
    
    ua = UserAgent()
    header = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36"}


    url = 'https://meteo.hr/podaci.php?section=podaci_vrijeme&param=europa_n'
    result = requests.get(url, headers=header).text

    doc = BeautifulSoup(result, "lxml")

    with open("./templates/page.html", "w", encoding="utf-8") as f:
        f.write(str(doc))

    with open("./templates/page.html", "r", encoding="utf-8") as f:
        rest = []
        for sub in f.readlines():
            rest.append(sub.replace("\n", "").strip())

        res = "".join(rest)


    doc = BeautifulSoup(res, "html.parser")


    tbody = doc.tbody
    trs = tbody.contents

    gradovi = {}
    vrijeme = {}


    for tr in trs:
        (city_name,
        wind_dir,
        wind_speed,
        temperature,
        current_conditions) = tr.contents

        fixed_city = str(city_name.string)

        gradovi[fixed_city] = {
            "Wind Direction": str(wind_dir.string),
            "Wind Speed": str(wind_speed.string) + " m/s",
            "Temperature": str(temperature.string) + " °C",
            "Current Conditions": str(current_conditions.string).capitalize()
        }
    
    return gradovi
    
app = Flask(__name__)


@app.route('/')
def index():
    cities = gradovi()
    return jsonify(cities)


app.run(debug=True)
