# Sample data
year = [1950, 1970, 1990, 2010, 2020]
pop = [2.5, 3.7, 5.3, 6.9, 7.8]  # in billions
gdp_cap = [500, 1000, 4000, 10000, 15000]  # GDP per capita
life_exp = [50.1, 60.2, 70.5, 75.3, 78.9]  # Life expectancy

# 1. Import matplotlib
import matplotlib.pyplot as plt

# 2. Print the last item from year and pop
print("Last year:", year[-1])
print("Last population:", pop[-1])

# 3. Line plot: year vs pop
plt.plot(year, pop)
plt.title("World Population Over Time")
plt.xlabel("Year")
plt.ylabel("Population (Billions)")
plt.grid(True)
plt.show()

# 4. Print the last item of gdp_cap and life_exp
print("Last GDP per capita:", gdp_cap[-1])
print("Last life expectancy:", life_exp[-1])

# 5. Line plot: gdp_cap vs life_exp
plt.plot(gdp_cap, life_exp)
plt.title("Life Expectancy vs GDP per Capita (Line Plot)")
plt.xlabel("GDP per Capita")
plt.ylabel("Life Expectancy")
plt.grid(True)
plt.show()

# 6. Scatter plot: gdp_cap vs life_exp
plt.scatter(gdp_cap, life_exp)
plt.xscale('log')  # Log scale for GDP
plt.title("Life Expectancy vs GDP per Capita (Scatter Plot)")
plt.xlabel("GDP per Capita (log scale)")
plt.ylabel("Life Expectancy")
plt.grid(True)
plt.show()

# 7. Scatter plot: pop vs life_exp
plt.scatter(pop, life_exp)
plt.title("Life Expectancy vs Population")
plt.xlabel("Population (Billions)")
plt.ylabel("Life Expectancy")
plt.grid(True)
plt.show()
