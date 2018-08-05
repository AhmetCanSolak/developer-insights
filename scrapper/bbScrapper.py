"""
This scripts takes data from the previously formed Github users database, and checks if those users also
have a bitbucket account - by checking if an account with the same username exists as a bitbucket user.
"""

import sqlite3
import requests

# Establish database connection
con = sqlite3.connect("githubusers.db", isolation_level=None, timeout=10)
cur = con.cursor()

# Create a list of usernames in the database
usernames = [ str(x)[2:-3:] for x in cur.execute("SELECT username FROM members").fetchall() ]

urlbase = "https://api.bitbucket.org/2.0/users/"
counter = 8589

# Check to see if the given username also exists as a bitbucket user. If yes, insert the user to the database
for username in usernames[15027::]:
    resp = requests.get(urlbase+username).json()
    if len(resp) == 10: # length = 10 implies user exists, length = 2 implies otherwise.
        cur.execute("INSERT INTO bbusers VALUES(\'%s\', \'%s\', \'%s\', \'%s\')" %
                    (username, resp["links"]["repositories"]["href"], resp["created_on"][:10], resp["location"]))
        counter += 1
        print(username, counter)


