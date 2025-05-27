import matplotlib.pyplot as plt

# Define categories and points
categories = [
    "Current Trend",
    "Tech Efficiency",
    "Economic Reality",
    "Generational Debt",
    "Environmental Pressure",
    "Likely Future"
]

optimistic_view = [9, 8, 5, 4, 3, 9]
realistic_view = [6, 6, 3, 2, 2, 5]

# Plotting
plt.figure(figsize=(12, 6))
plt.plot(categories, optimistic_view, marker='o', label='Industry Optimism')
plt.plot(categories, realistic_view, marker='o', label='Economic Reality')

# Chart styling
plt.title("The Air Travel Sustainability Gap: Optimism vs. Reality", fontsize=14)
plt.ylabel("Sustainability Score (1-10)", fontsize=12)
plt.ylim(0, 10)
plt.grid(True, linestyle='--', alpha=0.5)
plt.legend()
plt.xticks(rotation=30)

plt.tight_layout()
plt.show()
