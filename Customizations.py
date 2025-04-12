import matplotlib.pyplot as plt
import numpy as np

# Sample data for GDP per capita (x), life expectancy (y), population (bubble size), and color (continent)
gdp_cap = [974.5803384, 5937.029525, 6223.367465, 4797.231267, 12779.37964,
           34435.36744, 36126.4927, 29796.04834, 1391.253792, 33692.60508]
life_exp = [43.828, 76.423, 72.301, 42.731, 75.32,
            81.235, 79.829, 79.441, 64.698, 78.555]
pop = [89400000, 40900000, 82000000, 92000000, 7300000,
       64000000, 66000000, 70000000, 1310000000, 1300000000]  # Population
col = ['blue', 'yellow', 'green', 'red', 'yellow',
       'green', 'green', 'green', 'red', 'red']  # Continent colors

# Convert population to numpy array and double it for better bubble sizing
np_pop = np.array(pop) * 2

# Create the scatter plot
plt.figure(figsize=(10, 6))
plt.scatter(x=gdp_cap, y=life_exp, s=np_pop, c=col, alpha=0.8)

# Log scale for x-axis
plt.xscale('log')

# Axis labels and title
plt.xlabel('GDP per Capita [in USD]')
plt.ylabel('Life Expectancy [in years]')
plt.title('World Development in 2007')

# Custom tick marks for x-axis
tick_values = [1000, 10000, 100000]
tick_labels = ['1k', '10k', '100k']
plt.xticks(tick_values, tick_labels)

# Annotations
plt.text(1550, 65, 'India', fontsize=10)
plt.text(5800, 80, 'China', fontsize=10)

# Grid
plt.grid(True)

# Show the plot
plt.tight_layout()
plt.show()
