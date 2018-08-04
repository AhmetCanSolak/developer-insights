"""

scrap
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Rewrite.

:author: ClubRockers
:version: 1.0.1
:copyright: copyleft
:license: GPLv3

"""

# Dependency Injection
import json
import pprint

file = open("2015-01-01-15.json","r")
lines = file.readlines()
#events =[ (json.loads(line)) for line in lines]
print(lines[0])
pprint.pprint(json.loads(lines[0]))
