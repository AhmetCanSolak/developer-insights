"""
A script to plot the locations of users on the world map. Makes use of the Basemap toolkit of matplotlib.
"""
import sqlite3
from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
from geopy.geocoders import Nominatim

conn = sqlite3.connect(r"C:\Users\Ali\engr350-project\scrapper\githubusers.db")
cur = conn.cursor()

densities = { }
locations = list(filter(lambda x: x != 'None',
                        map(lambda x: x[0], cur.execute("SELECT location FROM glocations").fetchall())))
geolocator = Nominatim(user_agent="developer_insights")

total = 0

for loc in locations:
    if densities.__contains__(loc):
        densities[loc][0] += 1
        total += 1
    else:
        densities[loc] = [1]
        total += 1
print(densities)
removal = []

for location in list(densities.keys()):
    try:
        loc = geolocator.geocode(location)
        densities[location].append(loc.latitude)
        densities[location].append(loc.longitude)
        print(densities[location])
    except:
        removal.append(location) # bu çirkin şeyi yaptım çünkü concurrent modificationdan korkuyorum
        print("HATA VAR!!!!!!!!!!!!!!!!!!!!!!!!!!!1")
        continue

for lel in removal:
    densities.pop(lel)

lengths = [0] * len(densities)

for i in range(len(densities)):
    lengths[i] = float(list(densities.values())[i][0]) / total

print("lengths:", lengths)
lonlist = list(map(lambda x: x[1], densities.values()))
latlist = list(map(lambda x: x[2], densities.values()))

usermap = Basemap(projection='mill', resolution='l', lon_0=0)
# x,y = usermap(lonlist, latlist)
# print("lonlist", lonlist, "\n","latlist: ", latlist)
# print(x, "\n", y)
usermap.fillcontinents(color="green")
usermap.drawcoastlines()
usermap.drawcountries()
usermap.drawmapboundary(fill_color='aqua')
usermap.scatter(latlist, lonlist, s=list(map(lambda x: x*(10**3), lengths)), marker="o", color="mediumorchid", latlon=True, zorder=10)
plt.show()