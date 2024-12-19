# Problem: Given a time series dataset, decompose it into trend, seasonal, and residual components using classical decomposition or STL (Seasonal and Trend decomposition using Loess).



import pandas as pd
import matplotlib.pyplot as plt
import statsmodels
from statsmodels.tsa.seasonal import seasonal_decompose

# Sample data (time series)

data = {'Date': ['2024-01-01', '2024-02-01', '2024-03-01', '2024-04-01', '2024-05-01', '2024-06-01'],
        'Sales': [200, 250, 300, 350, 400, 450]}

df = pd.DataFrame(data)
df['Date'] = pd.to_datetime(df['Date'])
df.set_index('Date', inplace=True)

# Decompose the time series

decomposition = seasonal_decompose(df['Sales'], model="additive", period = 1)
print(decomposition)
