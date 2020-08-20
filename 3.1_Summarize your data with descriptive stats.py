import pandas as pd # Импорт Пандас как pd

# Import the data - чтение файла income
income = pd.read_csv('C:\\Users\\Dmitry\\Documents\\MEGA\\MEGAsync\\Python\\Курс DataCamp\\IMPORTING AND MANAGING FINANCIAL DATA IN PYTHON\\per_capita_income.csv')

# Inspect the result
income.info()

# Sort the data by income
income = income.sort_values('Income per Capita', ascending=False)

# Display the first and last five rows
print(income.mean())
print(income.median())
income['Income per Capita (,000)'] = income['Income per Capita'] // 1000 # новый столбец «Доход на душу населения (, 000)», равный доходу [«Доход на душу населения»] // 1000
income['Income per Capita (,000)'].mode() # mode для «Доход на душу населения»
