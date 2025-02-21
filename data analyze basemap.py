import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap

fig = plt.figure(figsize=(8, 8))

m = Basemap(projection='ortho', lon_0=50, lat_0=35, resolution='l')

m.drawcoastlines()
m.drawcountries()
m.fillcontinents(color='lightgray', lake_color='aqua')
m.drawmapboundary(fill_color='aqua')

cities = ['Tehran', 'Mashhad', 'Isfahan', 'Karaj', 'Shiraz',
          'Tabriz', 'Qom', 'Ahvaz', 'Kermanshah', 'Urmia']

lons = [51.38, 59.61, 51.66, 50.99, 52.58, 46.29, 50.87, 48.67, 47.07, 45.07]
lats = [35.68, 36.26, 32.65, 35.83, 29.59, 38.08, 34.63, 31.31, 34.32, 37.55]

x, y = m(lons, lats)

m.plot(x, y, marker='o', markersize=5, color='red',
       linestyle='-', linewidth=2, label="City Connections")

for city, xc, yc in zip(cities, x, y):
    plt.text(xc, yc, city, fontsize=10, ha='right', color='black')

plt.title("Most Populous Cities in Iran Connected on Earth")
plt.legend()
plt.show()
