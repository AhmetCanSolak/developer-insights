import http
import requests
import urllib3
from bs4 import BeautifulSoup

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

proxies = getproxies()
pindex = 0

urlbase = 'https://api.github.com/users?since='
idbase = 0

res = requests.get(urlbase + str(idbase))
print(res.json())

idbase=1

while len(res.json()) > 2:
<<<<<<< HEAD

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
                 # res = requests.get(urlbase + str(idbase), proxies=proxies[pindex])

        pindex += 1
        if pindex >= len(proxies):
            pindex = 0
            proxies = getproxies()
            # res = requests.get(urlbase + str(idbase), proxies=proxies[pindex])