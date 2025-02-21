# Plotting the most populous cities in Iran
import matplotlib.pyplot as plt


cities = ['Tehran', 'Mashhad', 'Isfahan', 'Karaj', 'Shiraz',
          'Tabriz', 'Qom', 'Ahvaz', 'Kermanshah', 'Urmia']

x = [51.38, 59.61, 51.66, 50.99, 52.58, 46.29, 50.87, 48.67, 47.07, 45.07]

y = [35.68, 36.26, 32.65, 35.83, 29.59, 38.08, 34.63, 31.31, 34.32, 37.55]

population = [14500000, 4000000, 3000000, 3000000, 2000000, 1850000, 1700000, 1650000, 1300000, 1200000]
pop=[y//1000 for y in population]

colors = ['red', 'blue', 'darkred', 'teal', 'seagreen',
          'gold', 'black', 'darkorange', 'mediumpurple', 'gray']


for n in range(len(cities)):
    plt.scatter(x[n], y[n], s=[pop[n]],
                color=colors[n], label=cities[n], alpha=0.5)

plt.title('10 biggest cities in Iran')
plt.xlabel('longtitude')
plt.ylabel('latitude')
plt.xticks(rotation=30)
plt.yticks(rotation=30)
plt.ylim([25.04, 39.87])
plt.xlim([44.03, 63.33])
plt.legend(markerscale=0.2, loc=4)
plt.show()
