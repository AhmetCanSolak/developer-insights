import sqlite3 as sqll3


# Connection initializations

# db1 = sqll3.connect("http://www.cansolak.com/engr350-project/scrapper/githubusers.db") # NOT WORKING
db = sqll3.connect("githubusers.db") # WORKING
cursor = db.cursor()

# Query, fetch and print the result
cursor.execute("SELECT Count(*) FROM members;")
# cursor.commit()

response = cursor.fetchall()
print(response)
