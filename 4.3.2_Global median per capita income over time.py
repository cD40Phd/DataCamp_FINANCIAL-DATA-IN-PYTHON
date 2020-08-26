# Мировой средний доход на душу населения с течением времени
# Функция seaborn barplot () показывает точечные оценки и доверительные интервалы в виде прямоугольных столбцов; 
# функция по умолчанию отображает среднее значение, но она также может представлять другую сводную статистику, 
# если вы передаете конкретную функцию numpy ее оценочному параметру:

# seaborn.barplot(x=None, y=None, data=None, estimator=<function mean>, ...)

# В этом упражнении вы будете использовать импортированный набор данных Всемирного банка, содержащий данные о мировом доходе на душу населения
# для 189 стран с 2000 года. Чтобы попрактиковаться в отображении сводной статистики по категориям, вы построите график и 
# сравните медианный глобальный доход на душу населения с 2000 года со средним значением.

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

xls = pd.ExcelFile('GNP_PCAP_PP.xls')
listing = pd.read_excel(xls, sheet_name='Data', na_values=['n/a'])

income_trend = listing

income_trend.info()
print('income_trend', income_trend.head())