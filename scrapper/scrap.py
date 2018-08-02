"""

scrap
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This python snippet written to fetch to users from Github API v3 and
it uses a list of proxies to exploit hourly request limits given by the
api.

:author: ClubRockers
:version: 1.0.1
:copyright: copyleft
:license: GPLv3

"""

# Dependency Injection
import http
import requests
import urllib3
from bs4 import BeautifulSoup

# A method to fetch a list of proxies with ports from a public service
# It returns a list of proxies fetched from sslproxies.org
def getproxies():
    proxiesHTML = requests.get('https://sslproxies.org/').text
    proxysoup = BeautifulSoup(proxiesHTML, 'html.parser')
    proxytable = proxysoup.find(id='proxylisttable')

    proxies = []

    for proxy in proxytable.tbody.find_all('tr'):
        proxies.append({
            'http': proxy.find_all('td')[0].string + ":" + proxy.find_all('td')[1].string,
            'https': proxy.find_all('td')[0].string + ":" + proxy.find_all('td')[1].string
        })
    return proxies

# Get the list of proxies
proxies = getproxies()
pindex = 0

urlbase = 'https://api.github.com/users?since='
idbase = 0

# Start crawling and print results
res = requests.get(urlbase + str(idbase))
print(res.json())

idbase=1

while len(res.json()) > 2:

        for i in range(50): # hourly unauthorized request limit is 60, trying 50 requests per ip
             try:
                for i in res.json():
                    print(i)
                idbase = i["id"]
                res = requests.get(urlbase + str(idbase), proxies=proxies[pindex])
             except:
                 pindex += 1
                 if pindex >= len(proxies):
                     pindex = 0
                     proxies = getproxies()
                 continue

        pindex += 1
        if pindex >= len(proxies):
            pindex = 0
            proxies = getproxies()
