# Обобщите категориальные переменные

# Категориальные переменные требуют другого подхода 
# Такие понятия, как средний, не имеют особого смысла
# Вместо этого мы будем полагаться на их частотное распределение.

# nunique() - это метод серии. Сколько уникадтных значений существует  для каждого из столбцов
# apply() - вызывать функцию для каждого столбца
# lambda : «анонимная функция», получает каждый столбец в качестве аргумента x

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#listings = pd.read_excel('listings.xlsx', sheet_name=['amex', 'nasdaq', 'nyse'], na_values=['n/a'])
#print('listings.info', listings)

#amex = listings['amex']

amex = pd.read_excel('listings.xlsx', sheet_name='amex', na_values=['n/a']) 

amex.info() 
# print(amex['Sector'].nunique())

# amex = amex['Sector'].nunique()
print('Sector nunique() = ', amex)

#amex[Sector].apply(lambda x: x.nunique())
amex.apply(lambda x: x.nunique())

# How many IPOs per year?
print('Как много IPO в год', amex['Sector'].value_counts())


# Convert IPO Year to int
ipo_by_yr = amex['IPO Year'].dropna().astype(int).value_counts()    # dropna() - избавиться от пропущенных значений; astype(int) - преобразовать остаток в целые числа
                                                                    # value_counts() - применённый к результату отображает правильные значения

print('Конвертируем в int','ipo_by_yr',ipo_by_yr)

# Visualiation
ipo_by_yr.plot(kind='bar', title='IPOs per Year') 
plt.xticks(rotation=45)

# Show the plot
plt.show()