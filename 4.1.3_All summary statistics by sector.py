# Вся сводная статистика по секторам

# Вы можете применить различную сводную статистику, о которой вы узнали в предыдущей главе, 
# к объекту groupby, чтобы получить результат для каждой категории. 
# Сюда входит функция .describe (), которая дает сразу несколько идей!

import pandas as pd

nasdaq = pd.read_excel('listings.xlsx', sheet_name='nasdaq', na_values=['n/a']) # читаем файл xlsx. Закладка 'amex'
nasdaq.info()

# Inspect NASDAQ data
nasdaq.info()

# Create market_cap_m
nasdaq['market_cap_m'] = nasdaq['Market Capitalization'].div(1e6)

# Drop the Market Capitalization column
nasdaq.drop('Market Capitalization', axis=1, inplace=True)
print('head()', nasdaq.head())

# Group nasdaq by Sector
nasdaq_by_sector = nasdaq.groupby('Sector')

# Group nasdaq by Sector
summary = nasdaq_by_sector.describe()

# Print the summary
print(summary)

# Unstack 
summary = summary.unstack()

# Print the summary again
print(summary)