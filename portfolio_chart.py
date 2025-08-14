import matplotlib.pyplot as plt
import numpy as np

# Assumptions
initial_rsu_value = 100_000  # RSUs vesting today
annual_growth_rate_stock = 0.12  # Annual return if holding the RSU stock
annual_growth_rate_index = 0.08  # Annual return if diversified into index fund
years = np.arange(0, 11, 1)

# Future value functions
def future_value(principal, rate, time):
    return principal * ((1 + rate) ** time)

# Calculating future values
stock_values = future_value(initial_rsu_value, annual_growth_rate_stock, years)
index_values = future_value(initial_rsu_value, annual_growth_rate_index, years)

# Plotting
plt.figure(figsize=(10, 6))
plt.plot(years, stock_values, label='Hold RSUs (Company Stock)', linestyle='dashdot', color='red')
plt.plot(years, index_values, label='Sell & Diversify (Index Fund)', linestyle='-', color='green')
plt.title('Comparing RSU Strategies: Hold vs. Sell & Diversify')
plt.xlabel('Years Since Vesting')
plt.ylabel('Portfolio Value ($)')
plt.legend()
plt.grid(True)
plt.tight_layout()
# Save instead of show
plt.savefig('portfolio_chart.png')
print("Plot saved as chart.png")
# plt.show()
