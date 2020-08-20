# Получите тикер крупнейшей компании по оказанию бытовых услуг

# Google Finance отказался от своего API, но теперь DataReader предоставляет доступ к источнику данных iex, который обеспечивает те же функции. 
# Чтобы экспериментировать с данными вне среды DataCamp, вам понадобится учетная запись IEX Cloud.
# Вместо индексации данных с помощью условного выражения вы также можете фильтровать по определенным значениям с помощью .loc [row_selector, column_selector]. 
# Кроме того, вы можете использовать .set_index (), чтобы задать конкретный столбец с уникальными значениями в качестве индекса DataFrame, и .idxmax (),
# чтобы вернуть индекс максимального значения.
# В этом упражнении вы примените эти методы выбора компаний, чтобы найти наиболее ценную компанию по оказанию потребительских услуг на любой из трех бирж, 
# и использовать ее тикер для построения тренда курса акций. DataReader, date, pandas as pd и matplotlib.pyplot as plt были импортированы, 
# как и DataFrame списков из последнего упражнения.

# Set the index of listings to Stock Symbol
listings_ss = listings.set_index('Stock Symbol')
listings_ss.info()
# Get ticker of the largest Consumer Services company
ticker = listings_ss.loc[listings_ss.Sector=='Consumer Services', 'Market Capitalization'].idxmax()

# Set the start date
start = date(2015,1,1)

# Import the stock data
data = DataReader(ticker,'iex',start)

# Plot close and volume
data[['close', 'volume']].plot(secondary_y='volume', title=ticker)

# Show the plot
plt.show()