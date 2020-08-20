#Сделайте листинг крупнейшей потребительской компании после 1998 г.

#Google Finance отказался от своего API, но теперь DataReader предоставляет доступ к источнику данных iex. Чтобы экспериментировать с данными 
#вне среды DataCamp, вам понадобится учетная запись IEX Cloud.
#Функциональность с использованием 'iex' такая же, за исключением того, что данные ограничены последними пятью годами, заголовки столбцов в нижнем регистре.

#Вы можете фильтровать свои данные по еще большему количеству условий, заключив каждое условие в круглые скобки и используя логические операторы,
#такие как & и |.
#Здесь вы узнаете, какая компания является крупнейшей компанией по оказанию потребительских услуг, которая стала публичной после Amazon в 1997 году. Данные содержатся в столбце «Год IPO»; Первичное публичное размещение (IPO) - это финансовое соглашение, описывающее первое публичное предложение акций частной компании.

#DataReader, date, pandas как pd и matplotlib.pyplot как plt были импортированы. Также доступны списки DataFrame из последнего упражнения.

# Set Stock Symbol as the index
listings = listings.set_index('Stock Symbol')

# Get ticker of the largest consumer services company listed after 1997
ticker = listings.loc[(listings.Sector == 'Consumer Services') & (listings['IPO Year'] > 1998), 'Market Capitalization'].idxmax()

# Set the start date
start = date(2015, 1, 1)

# Import the stock data
data = DataReader(ticker, 'iex', start)

# Plot close and volume
data[['close', 'volume']].plot(secondary_y='volume', title=ticker)

# Show the plot
plt.show()