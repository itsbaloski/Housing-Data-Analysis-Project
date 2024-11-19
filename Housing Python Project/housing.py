

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load housing data
housing_data = pd.read_csv('housing_data.csv')

# Check the columns
print(housing_data.columns)

# Descriptive statistics summary
print(housing_data['SalePrice'].describe())

# Histogram
sns.histplot(housing_data['SalePrice'])
plt.show()

# Perform log transformation on SalePrice data
housing_data['SalePrice'] = housing_data['SalePrice'].replace(0, np.nan)
log_data = np.log(housing_data['SalePrice'].dropna())
print("Log Skewness:", log_data.skew())
sns.histplot(log_data)
plt.show()

# Visualize 1st Floor Sq Feet vs. Sale Price
housing_data.plot.scatter(x='1stFlrSF', y='SalePrice', ylim=(0, 800000))
plt.show()

# Visualize Garage Area vs. Sale Price
housing_data.plot.scatter(x='GarageArea', y='SalePrice', ylim=(0, 800000))
plt.show()

# Visualize Year Built vs. Sale Price
f, ax = plt.subplots(figsize=(16, 8))
sns.boxplot(x='YearBuilt', y="SalePrice", data=housing_data, ax=ax)
ax.set_ylim(0, 800000)
plt.xticks(rotation=90)
plt.show()
