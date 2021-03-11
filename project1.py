import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from datetime import datetime


data = pd.read_csv('project1.csv', parse_dates=[ 'Date' ], index_col= [ 'Date' ] )
data.head()
print(data.shape)
print(data.describe())
#frequency = data.groupby(['Received Via'])
#print(frequency.describe())
#print(frequency['Received Via'].count())
print(data)
#print(data['2015-01-01':'2016-01-01'])
print(data.index)
print(data.Received)
weekly_resampled_data = data.Received.resample('W').count()
print("monthly_resampled_data", weekly_resampled_data)
#monthly_resampled_data1 = data.Received.resample('M').count()
plt.xlabel("Number of complaint weekly basis")
plt.ylabel("Number of frequency")
plt.title("Number of complaints at monthly and daily granularity levels")
plt.plot(weekly_resampled_data)
#Daily_resampled_data = data.Received.resample('D').count()
#plt.plot(Daily_resampled_data)
plt.show()




