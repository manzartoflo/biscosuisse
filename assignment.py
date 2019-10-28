# -*- coding: utf-8 -*-
"""
Created on Mon Oct 28 14:43:39 2019

@author: Sk Mobin
"""

from urllib.parse import urljoin
from bs4 import BeautifulSoup
import requests

url = "https://www.biscosuisse.ch/de/uber-uns/mitglieder/"
req = requests.get(url)
soup = BeautifulSoup(req.text, 'lxml')
tab = soup.findAll('div', {'class': 'container-fluid'})

file = open('assignment.csv', 'w')
header = "Name, Email, Phone, Fax, Website\n"
file.write(header)

for tabb in tab:
    name = tabb.findAll('h3')[0].text
    div = tabb.findAll('div', {'class': 'col-md-4'})
    try:
        tel, fax = div[1].text.lstrip().rstrip().split('\n')
    except:
        tel = div[1].text.lstrip().rstrip()
        fax = 'NaN'
    #print(tel.replace('Tel.', ''), fax.replace('Fax ', ''))
    aas = div[2].findAll('a')
    if(len(aas) == 2):
        email = aas[0].attrs['href'].replace('mailto:', '')
        web = aas[1].attrs['href']
    else:
        web = aas[0].attrs['href']
        email = 'NaN'
    print(email, web)
    file.write(name + ', ' + email + ', ' + tel + ', ' + fax + ', ' + web + '\n')
file.close()