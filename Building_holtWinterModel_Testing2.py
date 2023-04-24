import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.tsa.holtwinters import ExponentialSmoothing

# Generate random data for capacity planning
np.random.seed(1234)
data = pd.DataFrame(np.random.randint(100, 500, size=(60,1)), columns=["capacity"])
data.index = pd.date_range(start="2022-01-01", periods=len(data), freq="M")

# Split data into training and testing sets
train_data = data.iloc[:-12] # Use first 80% of data for training
test_data = data.iloc[-12:] # Use last 20% of data for testing

# Build Holt-Winters model
model = ExponentialSmoothing(train_data, seasonal_periods=12, trend='add', seasonal='add')
fitted_model = model.fit()

# Make predictions for future periods
forecast_data = fitted_model.forecast(12)
print(forecast_data)

# Plot training and test data, and model predictions
plt.figure(figsize=(12,6))
plt.plot(train_data.index, train_data.values, label="Training Data")
plt.plot(test_data.index, test_data.values, label="Test Data")
plt.plot(forecast_data.index, forecast_data.values, label="Forecast")

# Smooth out forecast using seasonal components
results = fitted_model.forecast(36)
smoothing_trend = results[-12:].values
smoothing_seasonal = results[-12:].values
smoothed_forecast = (forecast_data + smoothing_trend + smoothing_seasonal)
plt.plot(forecast_data.index, smoothed_forecast.values, label="Smoothed Forecast")
print(smoothing_trend)
print(smoothing_seasonal)
print(smoothed_forecast)
plt.legend()
plt.title("Holt-Winters Time Series Model for Capacity Planning")
plt.xlabel("Date")
plt.ylabel("Capacity")
plt.show()