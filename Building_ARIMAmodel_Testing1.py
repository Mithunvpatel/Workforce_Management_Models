import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.tsa.arima.model import ARIMA

##attach actual dataset to validate process

# Generate random data for capacity planning
np.random.seed(1234)
dates = pd.date_range(start="2022-01-01", periods=60, freq="d")
capacity = np.random.randint(100, 500, size=60)
data = pd.DataFrame({"capacity": capacity}, index=dates)

# Split data into training and testing sets
train_data = data.iloc[:-12] # Use first 80% of data for training
test_data = data.iloc[-12:] # Use last 20% of data for testing

# Build ARIMA model
model = ARIMA(train_data, order=(1,1,1))
fitted_model = model.fit()

# Make predictions for future periods
forecast_data = fitted_model.forecast(steps=12)

# Get rolling mean of forecast values over a window of 3
smoothed_forecast = forecast_data.rolling(window=3).mean()

#create a tooltip action on this dataplot

# Plot training and test data, and model predictions
fig, ax = plt.subplots(figsize=(12,6))
ax.plot(train_data, label="Training Data")
ax.plot(test_data, label="Test Data")
ax.plot(forecast_data, label="Forecast")
ax.plot(smoothed_forecast, label="Smoothed Forecast")
ax.legend()
ax.set_title("ARIMA Time Series Model for Capacity Planning")
ax.set_xlabel("Date")
ax.set_ylabel("Capacity")
plt.show()