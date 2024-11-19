# Housing Data Analysis Project

## Description

This project provides a detailed exploratory analysis of a housing dataset. The script investigates the relationships between various housing features and sale prices using statistical summaries, transformations, and visualizations.

## Files

1. `housing.py`
   - The primary script for data analysis and visualization.
   - Includes:
     - Loading and inspecting the dataset.
     - Performing a log transformation on sale price.
     - Creating visualizations to explore relationships between features like square footage, garage area, and year built with sale price.

2. `housing_data.csv`
   - The dataset used for analysis.
   - Contains housing attributes, including:
     - `SalePrice` (target variable)
     - `1stFlrSF` (first-floor square footage)
     - `GarageArea`
     - `YearBuilt`

3. `README.md`
   - Documentation for the project.

## Workflow

1. **Load Data**  
   Reads the `housing_data.csv` file using pandas.  
   `housing_data = pd.read_csv('housing_data.csv')`

2. **Inspect Data**  
   Displays column names and descriptive statistics of `SalePrice`.  
   `print(housing_data.columns)`  
   `print(housing_data['SalePrice'].describe())`

3. **Visualize Sale Price Distribution**  
   Plots a histogram to observe the distribution of sale prices.  
   `sns.histplot(housing_data['SalePrice'])`  
   `plt.show()`

4. **Log Transformation**  
   Reduces skewness in `SalePrice` by applying a log transformation.  
   `housing_data['SalePrice'] = housing_data['SalePrice'].replace(0, np.nan)`  
   `log_data = np.log(housing_data['SalePrice'].dropna())`  
   `sns.histplot(log_data)`  
   `plt.show()`

5. **Relationship Visualizations**
   - **First Floor Square Feet vs. Sale Price:**  
     Creates a scatter plot to analyze the relationship.  
     `housing_data.plot.scatter(x='1stFlrSF', y='SalePrice', ylim=(0, 800000))`

   - **Garage Area vs. Sale Price:**  
     Examines the correlation between garage size and sale price.  
     `housing_data.plot.scatter(x='GarageArea', y='SalePrice', ylim=(0, 800000))`

   - **Year Built vs. Sale Price:**  
     Uses a boxplot to visualize trends over time.  
     `f, ax = plt.subplots(figsize=(16, 8))`  
     `sns.boxplot(x='YearBuilt', y="SalePrice", data=housing_data, ax=ax)`  
     `ax.set_ylim(0, 800000)`  
     `plt.xticks(rotation=90)`  
     `plt.show()`

## Dependencies

- Python 3.8+
- Required libraries:
  - numpy
  - pandas
  - matplotlib
  - seaborn

Install dependencies with:  
`pip install numpy pandas matplotlib seaborn`

## Execution

1. Place `housing_data.csv` and `housing.py` in the same directory.
2. Run the script using:  
   `python housing.py`

## Outputs

- Histograms of sale price distributions (before and after log transformation).
- Scatter plots showing relationships between key housing features and sale price.
- A boxplot illustrating trends in sale prices by year built.

## License

This project is for educational and analytical purposes. You may modify and redistribute it as needed.
