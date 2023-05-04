import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.tsa.holtwinters import ExponentialSmoothing

#attach an actual dataset to validate process

# Generate random data for capacity planning
np.random.seed(1234)
dates = pd.date_range(start="2022-01-01", periods=60, freq="M")
capacity = np.random.randint(100, 500, size=60)
data = pd.DataFrame({"capacity": capacity}, index=dates)

# Split data into training and testing sets
train_data, test_data = data.iloc[:-12], data.iloc[-12:]

# Attach comparable model
# Build Holt-Winters model
model = ExponentialSmoothing(train_data, seasonal_periods=12, trend='add', seasonal='add').fit()

# Make predictions for future periods
forecast_data = model.forecast(12)

# Plot training and test data, and model predictions
fig, ax = plt.subplots(figsize=(12,6))
ax.plot(train_data, label="Training Data")
ax.plot(test_data, label="Test Data")
ax.plot(forecast_data, label="Forecast")
ax.legend()
ax.set_title("Holt-Winters Time Series Model for Capacity Planning")
ax.set_xlabel("Date")
ax.set_ylabel("Capacity")
plt.show()
