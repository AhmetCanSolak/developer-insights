"""
A script to search Github usernames of people one by one, and get their location data from responding json and
insert this info into the corresponding table (glocations) in the githubusers.db database
"""

import requests
import sqlite3
from bs4 import BeautifulSoup

con = sqlite3.connect("githubusers.db", isolation_level=None, timeout=10)
cur = con.cursor()

cur.execute("SELECT username FROM users")
usernames = cur.fetchall()

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
requestcounter = 0

urlbase = 'https://api.github.com/users/'

for username in usernames[3197::]:
    try:
        res = requests.get(urlbase + username[0], proxies=proxies[pindex])
        requestcounter += 1
        print(res.json())
        print("INSERT INTO glocations VALUES(\'%s\', \'%s\')" % (username[0], res.json()["location"]))
        cur.execute("INSERT INTO glocations VALUES(\'%s\', \'%s\')" % (username[0], res.json()["location"]))
        if requestcounter == 55:
            requestcounter = 0
            pindex += 1
            if pindex >= len(proxies):
                proxies = getproxies()
                pindex = 0
    except:
        pindex += 1
        if pindex >= len(proxies):
            proxies = getproxies()
            pindex = 0
        continue