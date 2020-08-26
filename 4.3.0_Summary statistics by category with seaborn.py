# countplot - график отображает кол-во наблюдений на категорию
# PointPlot - точечный график для сравнения статистики по нескольким категориальным переменным


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
print('combined_listings', combined_listings.head())
print('combined_listings', combined_listings.tail())
print('----------------------------------------')

nasdaq = combined_listings.loc[combined_listings['Exchange'] == 'nasdaq'] # используем метки столбцов и строк для доступа к данным с помощью .loc.
print(nasdaq)

# The basics: countplot
sns.countplot(x='Sector', data=nasdaq)
plt.xticks(rotation=45) 
plt.show() 

# countplot, sorted
sector_size = nasdaq.groupby('Sector').size() # выборка по размеру 'Sector'
order = sector_size.sort_values(ascending=False) # сортировка по значению 'Sector'
order.head() 
order = order.index.tolist() # Convert index to list


sns.countplot(x='Sector', data=nasdaq, order=order)
plt.xticks(rotation=45) 
plt.title('# Observations per Sector')
plt.show()

# countplot, multiple categories
plt.xticks(rotation=45)
recent_ipos = nasdaq[nasdaq['IPO Year'] > 2014] 
recent_ipos['IPO Year'] = recent_ipos['IPO Year'].astype(int)
sns.countplot(x='Sector', hue='IPO Year', data=recent_ipos)
plt.show()

# Compare stats with PointPlot
nasdaq['market_cap_m'] = nasdaq['Market Capitalization'].div(1e6)
nasdaq['IPO'] = nasdaq['IPO Year'].apply(lambda x: 'After 2000' if x > 2000 else 'Before 2000') 
sns.pointplot(x='Sector', y='market_cap_m', hue='IPO', data=nasdaq) 
plt.xticks(rotation=45); plt.title('Mean Market Cap') 
plt.show()