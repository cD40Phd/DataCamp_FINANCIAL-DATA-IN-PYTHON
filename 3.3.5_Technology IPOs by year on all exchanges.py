# Технологические IPO по годам на всех биржах

# Каждая компания в словаре листингов имеет год IPO в период с 1972 по 2017 год. Поэтому в этом контексте уместно рассматривать столбец 
# «Год IPO» на каждом листе как категориальную переменную с четко определенным порядком, даже если он имеет dtype float64.

# Здесь вы объедините данные со всех трех бирж и нанесете на график распределение лет IPO для компаний технологического сектора.


import pandas as pd
from datetime import date
import matplotlib.pyplot as plt


listings = pd.read_excel('listings.xlsx', sheet_name=['amex', 'nasdaq', 'nyse'], na_values=['n/a'])
# Create lists
exchanges = ['amex', 'nasdaq', 'nyse']
all_listings = []

# Use for loop to create listing_data
for exchange in exchanges:
    all_listings.append(listings[exchange])
    
# Combine DataFrames
listing_data = pd.concat(all_listings)
print('listing_data)',listing_data)

# Select tech companies
tech_companies = listing_data[listing_data.Sector == 'Technology']
print('tech_companies',tech_companies)

# Create ipo_years
ipo_years = tech_companies['IPO Year']
print('ipo_years', ipo_years)


# Drop missing values and convert to int
ipo_years = ipo_years.dropna().astype(int) 
print('ipo_years', ipo_years)