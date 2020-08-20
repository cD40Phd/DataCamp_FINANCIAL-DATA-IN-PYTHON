# Визуализация международного распределения доходов
#
# Seaborn — это более высокоуровневое API на базе библиотеки matplotlib. 
# Seaborn содержит более адекватные дефолтные настройки оформления графиков. 
# Если просто добавить в код import seaborn, то картинки станут гораздо симпатичнее. 
# Также в библиотеке есть достаточно сложные типы визуализации, которые в matplotlib 
# потребовали бы большого количество кода.
# https://nagornyy.me/courses/data-science/intro-to-seaborn/

# По умолчанию функция distplot () в пакете seaborn создает гистограмму, где данные 
# группируются в диапазоны и отображаются в виде столбцов, и соответствует оценке плотности ядра (KDE) 
# или сглаженной гистограмме. Вы также можете использовать distplot () для создания другого типа графика, 
# называемого rugplot, который добавляет маркеры в нижнюю часть диаграммы, чтобы указать плотность наблюдений по оси x.
#
# seaborn.distplot(a, bins=None, hist=True, kde=True, rug=False, ...)



from pandas_datareader.data import DataReader
import pandas as pd
from datetime import date
import matplotlib.pyplot as plt
import seaborn as sns


#ty10 = DataReader('DGS10', 'fred', date(1962, 1, 1)) 
#ty10.info() 
#print(ty10.describe())

#ty10.dropna(inplace=True)                           # Избегайте создания копии
#ty10.plot(title='10-year Treasury'); plt.tight_layout()
#sns.distplot(ty10)                                  # distplot одновременно показывает гистограмму и график плотности распределения.
#ax = sns.distplot(ty10) 
#ax.axvline(ty10['DGS10'].median(), color='pink', ls='-.')
#plt.show() 

income = pd.read_csv('C:\\Users\\Dmitry\\Documents\\MEGA\\MEGAsync\\Python\\Курс DataCamp\\IMPORTING AND MANAGING FINANCIAL DATA IN PYTHON\\per_capita_income.csv')

# Print the summary statistics for income
print(income.describe())

# Plot a basic histogram of income per capita
sns.distplot(income['Income per Capita']) 

# Show the plot
#plt.show()

# Plot a rugplot
sns.distplot(income['Income per Capita'], bins=50, kde=False, rug=True)

# Show the plot
plt.show()