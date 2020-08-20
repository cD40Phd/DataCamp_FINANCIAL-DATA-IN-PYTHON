#Получите данные для 3 крупнейших финансовых компаний

#Google Finance отказался от своего API, но теперь DataReader предоставляет доступ к источнику данных iex. Чтобы экспериментировать с данными вне среды DataCamp,
#вам понадобится учетная запись IEX Cloud.

#Функциональность с использованием 'iex' такая же, за исключением того, что данные ограничены последними пятью годами, заголовки столбцов имеют нижний регистр,
#а для нескольких тикеров возвращаемое значение представляет собой словарь, а не pandas.Panel. Мы включили в упражнение несколько строк кода, чтобы преобразовать
#словарь в DataFrame с MultiIndex, как в видео.
#У объекта pd.MultiIndex () более одного идентификатора на строку. Это позволяет получать данные на основе критериев сразу для нескольких компаний.

#Давайте применим этот новый навык, чтобы получить цены на акции крупнейших компаний финансового сектора. DataReader, date, pandas as pd и matplotlib.pyplot as plt 
#были импортированы, как и DataFrame списков из последнего упражнения.

import pandas as pd
from pandas_datareader.data import DataReader
from datetime import date

# Set Stock Symbol as the index
listings_ss = pd.read_excel('listings.xlsx', sheetname='nasdaq', na_values='n/a') 
listings_ss = listings.set_index('Stock Symbol')

# Get ticker of 3 largest finance companies
top_3_companies = listings_ss.loc[listings_ss.Sector == 'Finance', 'Market Capitalization'].nlargest(n=3)

# Convert index to list
top_3_tickers = top_3_companies.index.tolist()

# Set start date
start = date(2015,1,1)

# Set end date
end = date(2020,4,1)

# Import stock data
result = DataReader(top_3_tickers, 'iex', start, end)
result = result[~result.index.duplicated()]
data = pd.DataFrame()
