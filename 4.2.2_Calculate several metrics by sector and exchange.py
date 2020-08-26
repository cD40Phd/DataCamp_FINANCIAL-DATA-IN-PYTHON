# Рассчитайте несколько показателей по секторам и биржам

# Функция .agg () позволяет вам агрегировать ваши данные еще большим количеством способов, принимая два типа аргументов. 
# Предоставление списка имен статистических методов позволяет вычислить более одной сводной статистики одновременно, 
# а предоставление словаря, где ключи - это имена столбцов, а значения - статистические методы, применяет конкретную 
# сводную статистику к определенному столбцу.

import pandas as pd
import matplotlib.pyplot as plt
listings = []

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

# DataFrames listings
listings = combined_listings # это уже не Excel файл

# Create market_cap_m
listings['market_cap_m'] = listings['Market Capitalization'].div(1e6)

# Group listing by both Sector and Exchange
by_sector_exchange = listings.groupby(['Sector', 'Exchange'])

# Subset market_cap_m of by_sector_exchange
bse_mcm = by_sector_exchange['market_cap_m']

print(' - bse_mcm - ', by_sector_exchange.head())

# Calculate mean, median, and std in summary
summary = bse_mcm.agg({('Average', 'mean'), ('Median', 'median'), ('Standard Deviation', 'std')})

# Print the summary
print(' - summary - ', summary)