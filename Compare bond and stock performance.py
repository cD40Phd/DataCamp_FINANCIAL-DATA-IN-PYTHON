# Сравните доходность облигаций и акций
# Облигации и акции - самые важные инвестиционные альтернативы. Теперь, когда вы можете импортировать данные как из Федеральной резервной системы, 
# так и из Google Finance, вы можете сравнивать эффективность обоих классов активов. Вы будете использовать индекс общей доходности для каждого класса, 
# который учитывает доходность как от повышения цен, так и от выплат, таких как проценты или дивиденды.
# Для облигаций вы будете использовать значение индекса общей доходности высокой доходности в США от Bank of America Merrill Lynch ('BAMLHYH0A0HYM2TRIV').
# Для акций вы будете использовать индекс S&P 500 («SP500»). Оба они доступны в течение последних 10 лет службой FRED Федеральной резервной системы.
# В этом упражнении вы загрузите обе серии и сравните их эффективность. 

from pandas_datareader.data import DataReader 
from datetime import date
import matplotlib.pyplot as plt 

# Set the start date
start = date(2008,1,1)

# Set the series codes
series = ['BAMLHYH0A0HYM2TRIV', 'SP500']

# Import the data
data = DataReader(series, 'fred', start)

# Plot the results
data.plot(title='Performance Comparison',subplots=True)

# Show the plot
plt.show()