# Как описать рапределение наших данных 
# Квантили - это меры дисперсии, которые более устойчивы к выбросам. 
# Они делят данные на группы одинакогого размера, каждая из которых содержит определённый процент ваших данных
# КваРТили делят данные на четыре группы, каждая из которых содержит 25%
# Децили делят ваши дынные на 10 групп, каждая из которых содержит 10%
# Медиана соответсвует 2-му квартилю или 5-му децилю
# Межквартальный диаппазон это разница между 3-м и 1-м квартилем
# dot-describe metod использует percentiles для вычисления любого кваниля
# numpy-arange для создания списка значений от начала и до конца, разделённых шагом

import pandas as pd # Импорт Пандас как pd
import numpy as np
import matplotlib.pyplot as plt

# Import the data - чтение файла income
income = pd.read_csv('C:\\Users\\Dmitry\\Documents\\MEGA\\MEGAsync\\Python\\Курс DataCamp\\IMPORTING AND MANAGING FINANCIAL DATA IN PYTHON\\per_capita_income.csv')

print('Значение столбцов', income.columns) # columns - содержит информацию о названиях столбцов в наборе данных. 

# Inspect the result
income.info()
print('----------------------------------------------')
# Calculate mean
mean = income['Income per Capita'].mean()
print('mean', '\n', mean)

# Calculate median
median=income['Income per Capita'].median()
print('median', '\n', median)

#Доход в Индии
India = income.loc[income.Country=='India'] # - даёт доступ к элементу по строке и столбцу. 
# print(income[['Country', 'Income per Capita']].head(3))

India=India['Income per Capita']
print('----------------India-------------------------', '\n', India)
print('-------------median-India---------------------', '\n', median-India)

# Calculate standard deviation
std = income['Income per Capita'].std()

# Calculate and print lower and upper bounds
bounds = [(mean-std), (mean+std)]
print('верхнее и нижнее значение диаппазона', '\n', bounds)

# Calculate and print first and third quartiles
quantiles = income['Income per Capita'].quantile([0.25, 0.75])
print('Первая и третья квантилия'+'\n', quantiles)

# Calculate and print IQR
iqr = (quantiles[0.75] - quantiles[0.25])
print('межквартильный размах (IQR)', iqr)

# Generate range of deciles
quantiles = np.arange(.1, .91, .1)

# Print them
print(quantiles)

# Calculate deciles for 'Income per Capita'
deciles = income['Income per Capita'].quantile(np.arange(start=.1, stop=.91, step=.1))

# Print them
print(deciles)

# Plot deciles as a bar chart
deciles.plot(kind='bar', title='Global Income per Capita - Deciles')

# Make sure to use the tight layout!
plt.tight_layout()

# Show the plot
plt.show()