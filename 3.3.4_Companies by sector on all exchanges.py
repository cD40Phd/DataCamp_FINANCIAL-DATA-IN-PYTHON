# Компании по секторам на всех биржах

# Категориальная переменная - это переменная, которая является одним из ограниченного числа значений, основанных на некотором качественном свойстве. 
# Частотное распределение - это представление того, сколько раз встречается категориальная переменная.

# Вернитесь к биржевым данным из предыдущих глав. Функция .mean () НЕ ОЧЕНЬ полезна для понимания частоты значений «Сектор», 
# таких как «Технология» и «Финансы», тогда как .value_counts () и .nunique () - полезны.

# В этом упражнении вы сравните распределение листингов на AMEX, NASDAQ и NYSE по секторам.

import pandas as pd
from datetime import date
import matplotlib.pyplot as plt


listings = pd.read_excel('listings.xlsx', sheet_name=['amex', 'nasdaq', 'nyse'], na_values=['n/a'])
print('listings.info', listings)

# Create the list exchanges
exchanges = ['amex', 'nasdaq', 'nyse']

# Iterate over exchanges then plot and show result
for exchange in exchanges:
    sectors = listings[exchange].Sector.value_counts()

# Sort in descending order and plot
sectors.sort_values(ascending=False).plot(kind='bar')

# Show the plot
plt.show()