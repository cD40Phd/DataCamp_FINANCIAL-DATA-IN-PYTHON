# Выделение значений в раздаче

# Иногда необходимо манипулировать вашими данными, чтобы улучшить визуализацию. 
# Два метода, которые могут позаботиться о пропущенных значениях, - это .dropna () и .fillna (). 
# Вы также можете удалить выбросы, отфильтровав записи, превышающие или ниже определенного процентиля, 
# применив условие с помощью .quantile () к определенному столбцу.
import pandas as pd
from datetime import date
import matplotlib.pyplot as plt
import seaborn as sns

income = pd.read_csv('C:\\Users\\Dmitry\\Documents\\MEGA\\MEGAsync\\Python\\Курс DataCamp\\IMPORTING AND MANAGING FINANCIAL DATA IN PYTHON\\per_capita_income.csv')

# Create inc_per_capita
inc_per_capita = income['Income per Capita']

# Filter out incomes above the 95th percentile
inc_per_capita = inc_per_capita[inc_per_capita < inc_per_capita.quantile(.95)]

# Plot histogram and assign to ax
ax = sns.distplot(inc_per_capita)

# Highlight mean
ax.axvline(inc_per_capita.mean(), color='b')

# Highlight median
ax.axvline(inc_per_capita.median(), color='g')

# Show the plot
plt.show()