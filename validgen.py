# -*- coding: utf-8 -*-
"""
Created on Wed Mar  3 17:08:02 2021

@author: bryan
"""
import requests
import re
from bs4 import BeautifulSoup

names = []
urls = []
valid = []
urls.append("https://en.wikipedia.org/wiki/Glossary_of_computer_science")
#urls.append("https://en.wikipedia.org/wiki/Glossary_of_astronomy")
#urls.append("https://en.wikipedia.org/wiki/Glossary_of_physics")
#urls.append("https://en.wikipedia.org/wiki/Glossary_of_engineering")


for url in urls:
    htmlTxt = requests.get(url).text

    soup = BeautifulSoup(htmlTxt, 'html.parser')

    for i in soup.find_all("dt"):
        w = i.get('id')
        w = re.sub('_', '', w)
        names.append(w)

names.sort();

print('begin')

for user in names:
    try:
        if(requests.get(f'https://auth.roblox.com/v1/usernames/validate?request.username={user}&request.birthday=1337-04-20').json()['code']) == 0:
            print(user)
    except Exception as e:
        pass

print('done')
