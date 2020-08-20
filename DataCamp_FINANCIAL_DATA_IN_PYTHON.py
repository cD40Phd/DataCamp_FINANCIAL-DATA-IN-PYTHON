# Get stock data for a single company
# Import DataReader
from pandas_datareader.data import DataReader
from iexfinance.stocks import Stock
from datetime import date

a = Stock("AAPL", token="pk_23b9db2d9fb94c79bb71babaf37edcc7")
a.get_quote()

# Import date


# Set start and end dates
start = date(2016, 1, 1)
end = date(2016, 12, 31)

# Set the ticker
ticker = 'AAPL'

# Set the data source
data_source = 'iex'

# Import the stock prices
stock_prices = DataReader(ticker, data_source, start, end)

# Visualize a stock price trend

# Set the ticker and data_source
ticker = 'FB'
data_source = 'iex'

# Import the data using DataReader
stock_prices = DataReader(ticker, data_source, start, end)

stock_prices.info()

# Plot close
stock_prices['close'].plot(title=ticker)

# Show the plot
plt.show()
