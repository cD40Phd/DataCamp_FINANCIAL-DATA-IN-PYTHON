#Выберите 5 ведущих компаний-потребителей

#Как вы только что узнали, можно фильтровать акции на основе критериев с помощью метода sort_values () и аргумента ascending=False, 
#указывающего столбец для фильтрации. Кроме того, вы можете включить аргумент ascending = False для сортировки записей
#от самого высокого до самого низкого. Здесь вы воспользуетесь этой функцией, чтобы найти пять самых ценных компаний в 
#секторе потребительских услуг. Это измеряется рыночной капитализацией или совокупной стоимостью всех акций компании. 
#Pandas был импортирован как pd, как и DataFrame списков из первой главы. Напоминаем, что он содержит данные с AMEX, NYSE и NASDAQ.

# Select companies in Consumer Services
import pandas as pd
from pandas_datareader.data import DataReader
from datetime import date

start = date(2008,1,1)

# Set the series codes
series = ['All']

# Import the data

listings = DataReader() 

listings.head(5)
listings.info()

#consumer_services = listings[listings.Sector == 'Consumer Services']
#consumer_services.head()
# Sort consumer_services by market cap
#consumer_services2 = consumer_services.sort_values('Market Capitalization', ascending=False)

# Display first 5 rows of designated columns
# print(consumer_services2[['Company Name', 'Exchange', 'Market Capitalization']].head(5))