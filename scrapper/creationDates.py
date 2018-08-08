"""
A simple script to graph creation dates of the github users
"""

import sqlite3
import matplotlib.pyplot as plt

con = sqlite3.connect("githubusers.db")
cur = con.cursor()

cur.execute("SELECT date FROM bbusers")
dates = cur.fetchall()

years = {x: 0 for x in range(2008, 2019)}
months = {x: 0 for x in range(1, 9)}

for date in dates:
    year = int(date[0][0:4])
    years[year] += 1
    if year == 2018:
        month = int(date[0][6])
        months[month] += 1

years_x = list(years.keys())
years_y = list(years.values())
plt.bar(years_x, years_y)
plt.xlabel("Years")
plt.ylabel("# of registered users")
plt.show()

months_x = list(months.keys())
months_y = list(months.values())
plt.bar(months_x, months_y)
plt.xlabel("Months")
plt.ylabel("# of registered users")
plt.show()