import pandas as pd
from datetime import date
import matplotlib.pyplot as plt
import seaborn as sns

# Load the file into growth
growth = pd.read_csv('income_growth.csv', parse_dates=['DATE']).set_index('DATE')
growth.info()
print(growth.head())
print(growth.tail())

# Inspect the summary statistics for the growth rates
print(growth.describe())

# Iterate over the three columns
for column in growth.columns:
    sns.distplot(growth[column], hist=False, label=column)
    
# Show the plot
plt.show()
