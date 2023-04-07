import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

# Assuming that the energy data is returned in the following format
data = {'date': ['2022-01-01', '2022-01-02', '2022-01-03'],
        'energy_consumption': [1000, 1200, 800],
        'energy_production': [900, 1100, 700]}

# Convert date string to datetime format
data['date'] = [datetime.strptime(date, '%Y-%m-%d').date() for date in data['date']]

# Create a pandas DataFrame
df = pd.DataFrame(data)

# Calculate the energy balance
df['energy_balance'] = df['energy_production'] - df['energy_consumption']

# Plot the energy balance over time
plt.plot(df['date'], df['energy_balance'])
plt.xlabel('Date')
plt.ylabel('Energy Balance')
plt.title('Energy Balance over Time')
plt.show()
