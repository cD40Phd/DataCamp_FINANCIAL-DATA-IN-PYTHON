# Средняя рыночная капитализация по секторам

# Сводные данные - это данные, полученные в результате нескольких измерений. 
# Как вы узнали из видео, функция .groupby() полезна для агрегирования данных по определенной категории.

# Ранее вы видели, что данные о рыночной капитализации имеют большие выбросы. Чтобы получить более точную сводку 
# рыночной стоимости компаний в каждом секторе, вы рассчитаете медианную рыночную капитализацию по секторам.

import pandas as pd
# import numpy as np
import matplotlib.pyplot as plt

nyse = pd.read_excel('listings.xlsx', sheet_name='nyse', na_values=['n/a'])

# Inspect NYSE data
nyse.info()

# Create market_cap_m
nyse['market_cap_m'] = nyse['Market Capitalization'].div(1e6)

# Drop market cap column
nyse = nyse.drop('Market Capitalization', axis=1)

# Group nyse by sector
mcap_by_sector = nyse.groupby('Sector')

# Calculate median
median_mcap_by_sector = mcap_by_sector.market_cap_m.median()

# Plot and show as horizontal bar chart
median_mcap_by_sector.plot(kind='barh', title='NYSE - Median Market Capitalization')

# Add the label
plt.xlabel('USD mn')

# Show the plot
plt.show()