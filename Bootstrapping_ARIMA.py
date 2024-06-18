import numpy as np
import matplotlib.pyplot as plt
import statsmodels.api as sm

# Generate some random time series data
np.random.seed(0)
n_obs = 100
time = np.arange(n_obs)
data = np.random.normal(0, 1, n_obs)

# Fit a simple ARIMA model to the data
model = sm.tsa.ARIMA(data, order=(1, 1, 1))
results = model.fit()

# Forecast the next 10 time steps
n_forecast_steps = 10
forecast = results.forecast(steps=n_forecast_steps)

# Number of bootstrap samples
n_bootstraps = 1000

# Perform bootstrapping
bootstrap_forecasts = []
for _ in range(n_bootstraps):
    # Resample the data with replacement
    bootstrap_sample = np.random.choice(data, size=n_obs, replace=True)
    
    # Fit the model to the bootstrap sample
    bootstrap_model = sm.tsa.ARIMA(bootstrap_sample, order=(1, 1, 1))
    bootstrap_results = bootstrap_model.fit()
    
    # Forecast the next 10 time steps using the bootstrap model
    bootstrap_forecast = bootstrap_results.forecast(steps=n_forecast_steps)
    bootstrap_forecasts.append(bootstrap_forecast)

# Calculate the mean and standard deviation of the bootstrap forecasts
mean_forecast = np.mean(bootstrap_forecasts, axis=0)
std_dev_forecast = np.std(bootstrap_forecasts, axis=0)

# Plot the original data, point forecast, and confidence intervals
plt.figure(figsize=(10, 6))
plt.plot(time, data, label='Original Data')
plt.plot(time[-1] + np.arange(1, n_forecast_steps + 1), forecast, label='Point Forecast', color='red')
plt.fill_between(time[-1] + np.arange(1, n_forecast_steps + 1), mean_forecast - 1.96 * std_dev_forecast,
                 mean_forecast + 1.96 * std_dev_forecast, color='blue', alpha=0.2, label='95% CI')
plt.xlabel('Time')
plt.ylabel('Value')
plt.title('Bootstrapped Forecast with 95% Confidence Intervals')
plt.legend()
plt.grid(True)
plt.show()
