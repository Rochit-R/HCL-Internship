import numpy as np

temps = np.array([
    [30, 32, 33, 31, 29, 28, 30],  # City 1
    [25, 27, 26, 24, 28, 29, 27],  # City 2
    [35, 34, 36, 35, 37, 38, 36]   # City 3
])

avg_city_temp = np.mean(temps, axis=1)
print("Average temperature for each city:", avg_city_temp)

day3_temps = temps[:, 2]
print("Temperatures on Day 3:", day3_temps)

city1_last3 = temps[0, -3:]
print("City 1 last 3 days' temperatures:", city1_last3)