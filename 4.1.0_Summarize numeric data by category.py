# Обобщение числовых данных по категориям

# На данный момент: обобщите отдельные переменные
# Вычисление описательной статистики, такой как среднее значение, квантили
# Разделите данные на группы, затем объедините группы
# Примеры:
#   Крупнейшая компания по бирже
#   Медианная рыночная капитализация за год IPO
#   Средняя рыночная капитализация по сектору

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

nasdaq = pd.read_excel('listings.xlsx', sheet_name='nasdaq', na_values=['n/a']) # читаем файл xlsx. Закладка 'amex'
nasdaq.info()

# Группируйте данные по секторам
nasdaq['market_cap_m'] = nasdaq['Market Capitalization'].div(1e6) 
nasdaq = nasdaq.drop('Market Capitalization', axis=1) # Drop column 
nasdaq_by_sector = nasdaq.groupby('Sector') # Create groupby object 
#for sector, data in nasdaq_by_sector: 
#    print(sector, data.market_cap_m.mean())

# Сделайте это просто и пропустите цикл
mcap_by_sector = nasdaq_by_sector.market_cap_m.mean()
print(mcap_by_sector)

# Визуализация
title = 'NASDAQ = Avg. Market Cap by Sector' 
mcap_by_sector.plot(kind='barh', title=title)
plt.xlabel('USD mn') 
#plt.show()

# Сводная сводка по всем числовым столбцам
print('head()',nasdaq_by_sector.head())
print('mean()',nasdaq_by_sector.mean())
