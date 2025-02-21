import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap

fig = plt.figure(figsize=(10, 8))

m = Basemap(llcrnrlon=42, llcrnrlat=24, urcrnrlon=64, urcrnrlat=40,
            resolution='l', projection='lcc', lat_0=32, lon_0=53)

m.drawcoastlines()
m.drawcountries()
m.drawmapboundary(fill_color='aqua')
m.fillcontinents(color='lightgray', lake_color='aqua')

cities = ['Tehran', 'Mashhad', 'Isfahan', 'Karaj', 'Shiraz',
          'Tabriz', 'Qom', 'Ahvaz', 'Kermanshah', 'Urmia']

lons = [51.38, 59.61, 51.66, 50.99, 52.58, 46.29, 50.87, 48.67, 47.07, 45.07]
lats = [35.68, 36.26, 32.65, 35.83, 29.59, 38.08, 34.63, 31.31, 34.32, 37.55]

x, y = m(lons, lats)

m.plot(x, y, marker='o', markersize=6, color='red', linestyle='-', linewidth=2, label="City connections")

for city, xc, yc in zip(cities, x, y):
    plt.text(xc, yc, city, fontsize=10, ha='right', color='black')

plt.title("Most populous cities in Iran connected together")
plt.legend(loc=4)
plt.show()