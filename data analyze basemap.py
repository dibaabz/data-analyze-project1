import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap

# ایجاد یک شکل جدید
fig = plt.figure(figsize=(10, 8))

# تنظیم نقشه روی ایران با پروجکشن LCC (Lambert Conformal Conic)
m = Basemap(llcrnrlon=42, llcrnrlat=24, urcrnrlon=64, urcrnrlat=40,
            resolution='l', projection='lcc', lat_0=32, lon_0=53)

# رسم جزئیات نقشه
m.drawcoastlines()
m.drawcountries()
m.drawmapboundary(fill_color='aqua')
m.fillcontinents(color='lightgray', lake_color='aqua')

# داده‌های شهرها
cities = ['Tehran', 'Mashhad', 'Isfahan', 'Karaj', 'Shiraz',
          'Tabriz', 'Qom', 'Ahvaz', 'Kermanshah', 'Urmia']

lons = [51.38, 59.61, 51.66, 50.99, 52.58, 46.29, 50.87, 48.67, 47.07, 45.07]
lats = [35.68, 36.26, 32.65, 35.83, 29.59, 38.08, 34.63, 31.31, 34.32, 37.55]

# تبدیل مختصات طول و عرض جغرافیایی به سیستم نقشه
x, y = m(lons, lats)

# رسم شهرها و اتصال آن‌ها با خطوط
m.plot(x, y, marker='o', markersize=6, color='red', linestyle='-', linewidth=2, label="City Connections")

# افزودن نام شهرها
for city, xc, yc in zip(cities, x, y):
    plt.text(xc, yc, city, fontsize=10, ha='right', color='black')

# نمایش نقشه
plt.title("Most Populous Cities in Iran Connected together")
plt.legend()
plt.show()