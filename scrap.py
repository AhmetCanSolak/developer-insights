import requests

urlbase = 'https://api.github.com/users?since='
idbase = 0

res = requests.get(urlbase + str(idbase))

while len(res.json()) > 2:
    """for i in res.json():
        print(i)""" #buralar hep testti :D
    idbase = i["id"]
    res = requests.get(urlbase + str(idbase))
