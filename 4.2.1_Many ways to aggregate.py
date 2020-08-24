# Больше способов агрегировать

# Последний сегмент: группировка по одной переменной и агрегирование
# Более подробные способы обобщения ваших данных:
#  - Группировка по двум или более переменным
#  - Применить несколько агрегатов
# Примеры
#  - Средняя рыночная капитализация по секторам и годам IPO
#  - Среднее и стандартное отклонение курса акций по годам

# Стоимость компании по биржам и секторам
# Вы можете сгенерировать более подробные сводки ваших данных, предоставив список столбцов внутри .groupby () 
# и / или применив статистический метод, такой как .mean (), непосредственно к одному или нескольким числовым столбцам.

# Здесь вы рассчитаете среднюю рыночную капитализацию для каждого сектора, дифференцированную в зависимости от биржи, 
# на которой котируются компании. Вы также будете использовать .unstack () для поворота меток обмена из строк в столбцы. 
# Перед началом упражнения рекомендуется просмотреть списки на консоли!

import pandas as pd
import matplotlib.pyplot as plt

xls = pd.ExcelFile('C:\\Users\\Dmitry\\Documents\\MEGA\\MEGAsync\\Python\\Курс DataCamp\\IMPORTING AND MANAGING FINANCIAL DATA IN PYTHON\\listings.xlsx')
exchanges = xls.sheet_names
listings = []

# Use for loop to create listing_data
for exchange in exchanges:
    listing = pd.read_excel(xls, sheet_name=exchange)
    listing['Exchange'] = exchanges
    listings.append(listing)
# Combine three DataFrames
combined_listings = pd.concat(listings)

## DataFrames listings
#listings = combined_listings # это уже не Excel файл
#print('------------------------info()----------------------------------')
## Inspect listings
#listings.info()
#print('------------------------head()----------------------------------')
## Show listings head
#print(listings.head())
#print(listings.tail())
#print('----------------------------------------------------------------')

## Group listings by Sector and Exchange
#by_sector_exchange = listings.groupby(['Sector', 'Exchange'])

## Calculate the median market cap
#mcap_by_sector_exchange = by_sector_exchange.market_cap_m.median()

## Display the head of the result
#print(mcap_by_sector_exchange.head())

## Unstack mcap_by_sector_exchange
#mcap_unstacked = mcap_by_sector_exchange.unstack()

## Plot as a bar chart
#mcap_unstacked.plot(kind='bar', title='Median Market Capitalization by Exchange')

## Set the x label
#plt.xlabel('USD mn')

## Show the plot
#plt.show()