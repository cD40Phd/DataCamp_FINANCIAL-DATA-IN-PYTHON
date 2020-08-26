# Постройте график IPO для всех бирж с помощью countplot ()
# Чтобы создать базовую визуализацию количества наблюдений для каждой категории в наборе данных,
# обычно подходит функция seaborn countplot ():
# seaborn.countplot(x=None, hue=None, data=None, ...)
# Параметр x содержит имена переменных в аргументе данных, который представляет собой DataFrame для построения графика. 
# hue определяет дополнительную категориальную переменную с цветом. 
# Это три необязательных параметра из многих, принимаемых функцией; 
# для получения полного списка ознакомьтесь с документацией по seaborn.

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
listings = []
nasdaq = []

xls = pd.ExcelFile('listings.xlsx')
exchanges = xls.sheet_names

# Use for loop to create listing_data
for exchange in exchanges:
    listing = pd.read_excel(xls, sheet_name=exchange)
    # Add reference col
    listing['Exchange'] = exchange
    # Add DataFrame to list
    listings.append(listing)

# Combine three DataFrames
combined_listings = pd.concat(listings)
combined_listings.info()

listings = combined_listings

# Select IPOs after 2000
listings = listings[listings['IPO Year'] > 2000]

# Convert IPO Year to integer
listings['IPO Year'] = listings['IPO Year'].astype(int)

# Create a countplot
sns.countplot(x='IPO Year', hue='Exchange', data=listings)

# Rotate xticks and show result
plt.xticks(rotation=45)

# Show the plot
plt.show()