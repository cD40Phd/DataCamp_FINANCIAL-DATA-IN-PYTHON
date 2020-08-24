# Медианная рыночная капитализация по годам IPO

# На последнем уроке предыдущей главы вы создали график количества IPO в год для технологических компаний.

# Теперь давайте проанализируем, как менялась рыночная капитализация за разные годы IPO. Вы можете объединить 
# данные со всех трех бирж, чтобы получить более полное представление.

# включает добавленный справочный столбец «exchange», содержащий exchange для каждой перечисленной компании.

import pandas as pd
# import numpy as np
import matplotlib.pyplot as plt

listings = pd.read_excel('listings.xlsx', sheet_name=['amex', 'nasdaq', 'nyse'], na_values=['n/a'])
print('listings', listings)

exchanges = ['amex', 'nasdaq', 'nyse']
all_listings = []

# Use for loop to create listing_data
for exchange in exchanges:
    all_listings.append(listings[exchange])
    
# Combine DataFrames
listings = pd.concat(all_listings) # это уже не Excel файл
print('------------------------info()----------------------------------')
# Inspect listings
listings.info()
print('------------------------head()----------------------------------')
# Show listings head
print(listings.head())
print('----------------------------------------------------------------')

# Create market_cap_m
listings['market_cap_m'] = listings['Market Capitalization'].div(1e6)

# Select companies with IPO after 1985
listings = listings[listings['IPO Year'] > 1985]

# Drop missing values and convert to integers
listings['IPO Year'] = listings['IPO Year'].dropna().astype(int)

# Calculate the median market cap by IPO Year and sort the index
ipo_by_year = listings.groupby('IPO Year').market_cap_m.median().sort_index()

# Plot results as a bar chart
ipo_by_year.plot(kind='bar')

# Show the plot
plt.show()