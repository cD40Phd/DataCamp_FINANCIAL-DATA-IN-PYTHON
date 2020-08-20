#Compare labor market participation and unemployment rates
#Two economic data series in FRED are the Civilian Unemployment Rate ('UNRATE') and the Civilian Labor Force Participation Rate ('CIVPART').
#These rates highlight two important aspects of the US labor market: the share of the civilian population that is currently unemployed or seeking employment, and the share of those active in the labor market that are in fact employed.
#This means that the numbers indicate both the size of the labor market relative to the total population, as well as the size of unemployment relative to the labor market.
#Here, you will import, modify, and plot the data. DataReader, date, pandas as pd, and matplotlib.pyplot as plt have been imported.

# Set the start date
from pandas_datareader.data import DataReader 
from datetime import date
import matplotlib.pyplot as plt 

start = date(2017,1,1)

# Define the series codes
series = ['UNRATE', 'CIVPART']

# Import the data
econ_data = DataReader(series, 'fred', start)

# Assign new column labels
econ_data.columns = ['Unemployment Rate', 'Participation Rate']

# Plot econ_data
econ_data.plot(title='Labor Market',subplots=True)

# Show the plot
plt.show()
