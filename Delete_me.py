import pandas as pd

# Data provided
data = {
    'Month': ['January', 'February', 'March', 'April', 'May', 'June', 
              'July', 'August', 'September', 'October', 'November', 'December'],
    'Active Users': [152891, 152551, 147286, 147286, 147826, 143291,
                     143357, 148956, 144546, 167046, 171546, 173796]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Set Month as index (optional, but helps with time series analysis)
df['Month'] = pd.to_datetime(df['Month'], format='%B').dt.month
df = df.set_index('Month')

# Plot to visualize the data and check for seasonality
import matplotlib.pyplot as plt

plt.figure(figsize=(10, 6))
plt.plot(df.index, df['Active Users'], marker='o', linestyle='-')
plt.title('Active Users Over Months')
plt.xlabel('Month')
plt.ylabel('Active Users')
plt.xticks(range(1, 13), df.index, rotation=45)
plt.grid(True)
plt.show()

import numpy as np

# Calculate the average active users
average_active_users = np.mean(df['Active Users'])

# Create a forecast DataFrame
forecast_df = pd.DataFrame({
    'Month': pd.date_range(start='2024-01-01', periods=12, freq='M').strftime('%B'),
    'Forecasted Chats': [average_active_users] * 12
})

print(forecast_df)


